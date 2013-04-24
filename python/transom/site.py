#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

import fnmatch
import markdown2
import os
import shutil
import sys
import tempfile

from ConfigParser import SafeConfigParser
from collections import defaultdict
from urllib2 import urlopen
from urlparse import urlsplit, urljoin
from xml.etree.ElementTree import XML

class Site(object):
    def __init__(self, url, input_dir, output_dir):
        self.url = url
        self.input_dir = input_dir
        self.output_dir = output_dir

        self.config_path = os.path.join(self.input_dir, "site.conf")
        self.template_path = os.path.join(self.input_dir, "template.html")

        extras = {
            "wiki-tables": True,
            "code-friendly": True,
            "header-ids": True,
            "markdown-in-html": True,
            }

        self.markdown = markdown2.Markdown(extras=extras)

        self.config = SafeConfigParser()
        self.template_content = None

        self.files = list()
        self.files_by_input_path = dict()

        self.resources = list()
        self.pages = list()

        self.links = defaultdict(set)
        self.targets = set()

    def init(self):
        self.config.read(self.config_path)

        with open(self.template_path, "r") as file:
            self.template_content = file.read()

        self.traverse_input_pages(self.input_dir, None)
        self.traverse_input_resources(self.input_dir)

        for file in self.files:
            file.init()

    def render(self):
        for page in self.pages:
            page.read_input()
            page.convert()

        for page in self.pages:
            page.process()

        for page in self.pages:
            page.render()
            page.write_output()

        for resource in self.resources:
            resource.copy_to_output()

    def check_links(self, internal=True, external=False):
        for page in self.pages:
            page.read_output()

        for page in self.pages:
            page.check_links()

        errors_by_link = defaultdict(list)

        for link in self.links:
            if internal and link.startswith(self.url):
                if link not in self.targets:
                    errors_by_link[link].append("Link has no target")

            if external and not link.startswith(self.url):
                code, error = self.check_external_link(link)
            
                if code >= 400:
                    errors_by_link[link].append("HTTP error code {}".format(code))

                if error:
                    errors_by_link[link].append(error.message)

            sys.stdout.write(".")
            sys.stdout.flush()

        print

        for link in errors_by_link:
            print "Link: {}".format(link)

            for error in errors_by_link[link]:
                print "  Error: {}".format(error)

            for source in self.links[link]:
                print "  Source: {}".format(source)

    def check_external_link(self, link):
        code, error = None, None

        try:
            sock = urlopen(link, timeout=5)
            code = sock.getcode()
        except IOError as e:
            error = e
        finally:
            sock.close()

        return code, error

    def traverse_input_pages(self, dir, page):
        names = set(os.listdir(dir))

        if ".transom-skip" in names:
            return

        for name in ("index.md", "index.html", "index.html.in"):
            if name in names:
                names.remove(name)
                page = _Page(self, os.path.join(dir, name), page)
                break

        for name in sorted(names):
            path = os.path.join(dir, name)

            if os.path.isfile(path):
                for extension in (".md", ".html.in", ".html"):
                    if name.endswith(extension):
                        _Page(self, path, page)
                        break
            elif os.path.isdir(path) and name not in (".svn"):
                self.traverse_input_pages(path, page)

    def traverse_input_resources(self, dir):
        names = set(os.listdir(dir))

        for name in sorted(names):
            path = os.path.join(dir, name)

            if os.path.isfile(path):
                if path not in self.files_by_input_path:
                    _Resource(self, path)
            elif os.path.isdir(path) and name not in (".svn"):
                self.traverse_input_resources(path)

    def get_output_path(self, input_path):
        path = input_path[len(self.input_dir) + 1:]
        return os.path.join(self.output_dir, path)

    def get_url(self, output_path):
        path = output_path[len(self.output_dir) + 1:]
        path = "/".join(path.split(os.path.sep))
        return "{}/{}".format(self.url, path)

class _File(object):
    def __init__(self, site, input_path):
        self.site = site
        self.input_path = input_path
        self.output_path = self.site.get_output_path(self.input_path)
        self.url = self.site.get_url(self.output_path)

        self.site.files.append(self)
        self.site.files_by_input_path[self.input_path] = self

    def init(self):
        self.site.targets.add(self.url)

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.input_path)

class _Resource(_File):
    def __init__(self, site, input_path):
        super(_Resource, self).__init__(site, input_path)

        self.site.resources.append(self)

    def copy_to_output(self):
        _make_dirs(os.path.dirname(self.output_path))
        shutil.copy(self.input_path, self.output_path)

class _Page(_File):
    def __init__(self, site, input_path, parent):
        super(_Page, self).__init__(site, input_path)

        self.parent = parent

        self.content = None
        self.title = None

        self.site.pages.append(self)

    def init(self):
        if self.output_path.endswith(".md"):
            self.output_path = "{}.html".format(self.output_path[:-3])
            self.convert = self.convert_from_markdown
        elif self.output_path.endswith(".html.in"):
            self.output_path = self.output_path[:-3]
            self.convert = self.convert_from_html_in

        self.url = self.site.get_url(self.output_path)

        super(_Page, self).init()

    def read_input(self):
        with open(self.input_path, "r") as file:
            self.content = file.read()

    def write_output(self, path=None):
        if path is None:
            path = self.output_path

        _make_dirs(os.path.dirname(path))

        with open(path, "w") as file:
            file.write(self.content)

    def read_output(self):
        with open(self.output_path, "r") as file:
            self.content = file.read()

    def convert(self):
        pass

    def convert_from_markdown(self):
        # Strip out comments
        content_lines = self.content.splitlines()
        content_lines = (x for x in content_lines if not x.startswith(";;"))

        content = os.linesep.join(content_lines)
        content = self.site.markdown.convert(content)

        self.content = self.apply_template(content)

    def convert_from_html_in(self):
        self.content = self.apply_template(self.content)

    def apply_template(self, content):
        return self.site.template_content.replace("@content@", content)

    def process(self):
        self.title = os.path.split(self.output_path)[1]

        root = self.parse_xml(self.content)
        elem = root.find(".//{http://www.w3.org/1999/xhtml}h1")

        if elem is None:
            elem = root.find(".//{http://www.w3.org/1999/xhtml}h2")

        if elem is not None:
            self.title = "".join(elem.itertext())

        self.title = self.title.strip()
        self.title = _ascii(self.title)

    def parse_xml(self, xml):
        try:
            return XML(xml)
        except Exception as e:
            path = tempfile.mkstemp(".xml")[1]
            msg = "{} fails to parse; {}; see {}".format(self, str(e), path)

            with open(path, "w") as file:
                file.write(xml)

            raise Exception(msg)

    def render(self):
        path_nav = self.render_path_navigation()

        self.content = self.content.replace("@path-navigation@", path_nav)
        self.content = self.content.replace("@title@", self.title)

        overrides = dict()
        overrides["site-url"] = self.site.url

        for name, value in self.site.config.items("main", vars=overrides):
            self.content = self.content.replace("@{}@".format(name), value)

    def render_link(self):
        return "<a href=\"{}\">{}</a>".format(self.url, self.title)

    def render_path_navigation(self):
        links = list()
        page = self.parent

        links.append(self.title)

        while page and page.parent:
            links.append(page.render_link())
            page = page.parent

        links = "".join(("<li>{}</li>".format(x) for x in reversed(links)))

        return "<ul id=\"path-navigation\">{}</ul>".format(links)

    def check_links(self):
        root = self.parse_xml(self.content)

        links = self.gather_links(root)
        targets = self.gather_targets(root)

        for link in links:
            if link == "?":
                continue

            scheme, netloc, path, query, fragment = urlsplit(link)

            if scheme and scheme not in ("http", "https", "ftp"):
                continue

            if netloc in ("issues.apache.org", "bugzilla.redhat.com"):
                continue

            if (fragment and not path) or not path.startswith("/"):
                link = urljoin(self.url, link)

            self.site.links[link].add(self.url)

        self.site.targets.update(targets)

    def gather_links(self, root_elem):
        links = set()

        for elem in root_elem.iter("*"):
            for name in ("href", "src", "action"):
                try:
                    link = elem.attrib[name]
                except KeyError:
                    continue

                links.add(link)

        return links

    def gather_targets(self, root_elem):
        targets = set()

        for elem in root_elem.iter("*"):
            try:
                id = elem.attrib["id"]
            except KeyError:
                continue

            target = "{}#{}".format(self.url, id)

            assert target not in targets, target

            targets.add(target)

        return targets

def _ascii(string):
    if isinstance(string, unicode):
        return string.encode("ascii", "xmlcharrefreplace")

    return string

def _make_dirs(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
