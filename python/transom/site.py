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

        self.pages = list()
        self.pages_by_site_path = dict()

        self.files = list()

        self.links = defaultdict(set)
        self.targets = set()

    def init(self):
        self.config.read(self.config_path)

        with open(self.template_path, "r") as file:
            self.template_content = file.read()

        self.traverse_inputs(self.input_dir, None, False)

        for page in self.pages:
            page.init()

    def render(self):
        for page in self.pages:
            page.read_input()
            page.convert()

        for page in self.pages:
            page.process()

        for page in self.pages:
            page.render()
            page.write_output()

        for file in self.files:
            self.copy_file_to_output(file)

    def check(self):
        for page in self.pages:
            page.check()

        for link in self.links:
            errors = list()

            if link.startswith(self.url):
                if link not in self.targets:
                    errors.append("Link has no target")

            if errors:
                print "Link: {}".format(link)

                for error in errors:
                    print "  Warning: {}".format(error)

                for source in self.links[link]:
                    print "  Source: {}".format(source)

    def traverse_inputs(self, dir, page, skipped):
        names = set(os.listdir(dir))

        if ".transom-skip" in names:
            skipped = True

        for name in names:
            path = os.path.join(dir, name)

            if os.path.isfile(path):
                for extension in (".md", ".html.in", ".html"):
                    if not skipped and name.endswith(extension):
                        _Page(self, page, dir, name)
                        break
                else:
                    self.files.append(os.path.join(dir, name))
            elif os.path.isdir(path):
                if name not in (".svn"):
                    self.traverse_inputs(path, page, skipped)

    def copy_file_to_output(self, input_path):
        output_path = self.get_output_path(input_path)
        output_dir = os.path.split(output_path)[0]

        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)

        shutil.copy(input_path, output_path)

        site_path = self.get_site_path(output_path)
        self.targets.add(self.get_url(site_path))

    def get_output_path(self, input_path):
        path = input_path[len(self.input_dir) + 1:]
        return os.path.join(self.output_dir, path)

    def get_site_path(self, output_path):
        path = output_path[len(self.output_dir) + 1:]
        return "/".join(path.split(os.path.sep))

    def get_url(self, site_path):
        return "{}/{}".format(self.url, site_path)

class _Page(object):
    def __init__(self, site, parent, input_dir, input_name):
        self.site = site
        self.parent = parent
        self.input_dir = input_dir
        self.input_name = input_name
        self.input_path = os.path.join(self.input_dir, self.input_name)

        self.output_path = None
        self.site_path = None
        self.url = None

        self.input = None
        self.output = None

        self.root_elem = None
        self.title = None

        self.site.pages.append(self)

    def init(self):
        self.output_path = self.site.get_output_path(self.input_path)

        if self.input_path.endswith(".md"):
            self.output_path = "{}.html".format(self.output_path[:-3])
            self.convert = self.convert_from_markdown
        elif self.input_path.endswith(".html.in"):
            self.output_path = self.output_path[:-3]
            self.convert = self.convert_from_html_in

        self.site_path = self.site.get_site_path(self.output_path)
        self.url = self.site.get_url(self.site_path)

        self.site.pages_by_site_path[self.site_path] = self

    def read_input(self):
        with open(self.input_path, "r") as file:
            self.input = file.read()

    def convert(self):
        self.output = self.input

    def convert_from_markdown(self):
        # Strip out comments
        input_lines = self.input.splitlines()
        input_lines = (x for x in input_lines if not x.startswith(";;"))

        content = os.linesep.join(input_lines)
        content = self.site.markdown.convert(content)

        self.output = self.apply_template(content)

    def convert_from_html_in(self):
        self.output = self.apply_template(self.input)

    def apply_template(self, content):
        return self.site.template_content.replace("@content@", content)

    def process(self):
        self.parse_xml(self.output)

        self.title = os.path.split(self.output_path)[1]

        for elem in self.root_elem.iter("{http://www.w3.org/1999/xhtml}h1"):
            self.title = " ".join(elem.itertext())
            break

        self.title = self.title.strip()

    def parse_xml(self, input):
        try:
            self.root_elem = XML(self.output)
        except Exception as e:
            path = tempfile.mkstemp(".xml")[1]
            self.write_output(path)
            error("{} fails to parse; {}; see {}", self, str(e), path)

    def render(self):
        path_nav = self.render_path_navigation()

        self.output = self.output.replace("@path-navigation@", path_nav)
        self.output = self.output.replace("@title@", self.title)

        overrides = dict()
        overrides["site-url"] = self.site.url

        for name, value in self.site.config.items("main", vars=overrides):
            self.output = self.output.replace("@{}@".format(name), value)

    def render_link(self):
        return "<a href=\"{}\">{}</a>".format(self.url, self.title)

    def render_path_navigation(self):
        path_names = self.site_path.split("/")
        links = list()

        for i in range(1, len(path_names)):
            item_names = path_names[0:i]
            item_names.append("index.html")

            item_site_path = os.path.join(*item_names)

            try:
                page = self.site.pages_by_site_path[item_site_path]
            except KeyError:
                continue

            if page is self:
                links.append(self.title)
            else:
                links.append(page.render_link())

        if path_names[-1] != "index.html":
            links.append(self.title)

        links = "".join(("<li>{}</li>".format(x) for x in links))

        return "<ul id=\"path-navigation\">{}</ul>".format(links)

    def check(self):
        # Reparse to pick up new attr values after substitutions
        self.parse_xml(self.output)

        links = self.gather_links()
        targets = self.gather_targets()

        for link in links:
            scheme, netloc, path, query, fragment = urlsplit(link)

            if link == "?":
                continue

            if scheme in ("mailto", "irc"):
                continue

            if (fragment and not path) or not path.startswith("/"):
                link = urljoin(self.url, link)

            self.site.links[link].add(self.url)

        self.site.targets.update(targets)

    def gather_links(self):
        links = set()

        for elem in self.root_elem.iter("*"):
            for name in ("href", "src", "action"):
                try:
                    link = elem.attrib[name]
                except KeyError:
                    continue

                links.add(link)

        return links

    def gather_targets(self):
        targets = set()
        targets.add(self.url)

        for elem in self.root_elem.iter("*"):
            try:
                id = elem.attrib["id"]
            except KeyError:
                continue

            target = "{}#{}".format(self.url, id)

            assert target not in targets, target

            targets.add(target)

        return targets

    def write_output(self, path=None):
        if path is None:
            path = self.output_path

        output_dir = os.path.dirname(path)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(path, "w") as file:
            file.write(self.output)

    def __repr__(self):
        args = self.__class__.__name__, self.input_dir, self.input_name
        return "{}({},{})".format(*args)
