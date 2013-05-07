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

from script import *

def export_release(release, output_dir=None):
    if output_dir is None:
        temp_dir = make_user_temp_dir()
        output_dir = join(temp_dir, "qpid-{}".format(release))

    if exists(join(output_dir, "QPID_VERSION.txt")):
        debug("Export already exists")
        return output_dir

    call("svn --version")

    assert not exists(output_dir)

    url = "http://svn.apache.org/repos/asf/qpid/branches/{}/qpid".format(release)
    call("svn export {} {}", url, output_dir)

    return output_dir

def export_proton_release(release, output_dir=None):
    if output_dir is None:
        temp_dir = make_user_temp_dir()
        output_dir = join(temp_dir, "qpid-proton-{}".format(release))

    if exists(join(output_dir, "version.txt")):
        debug("Export already exists")
        return output_dir

    call("svn --version")

    assert not exists(output_dir)

    url = "http://svn.apache.org/repos/asf/qpid/proton/branches/{}".format(release)
    call("svn export {} {}", url, output_dir)

    return output_dir

_doxygen_conf_template = u"""
DISABLE_INDEX = yes
EXTRACT_ALL = yes
GENERATE_LATEX = no
GENERATE_TREEVIEW = yes
HAVE_DOT = yes
PROJECT_NUMBER = {release}
QUIET = yes
RECURSIVE = yes
INPUT = {input_paths}
PROJECT_NAME = "{title}"
STRIP_FROM_PATH = {strip_paths}
HTML_OUTPUT = {output_dir}
"""

def gen_doxygen(release, title, input_paths, strip_paths, output_dir):
    input_paths = " ".join(input_paths)
    strip_paths = " ".join(strip_paths)

    make_dirs(output_dir)

    conf = _doxygen_conf_template.format(**locals())
    path = write_entry("conf", conf)

    call("doxygen {}", path)

    touch(join(output_dir, ".transom-skip"))

def gen_epydoc(release, title, input_paths, input_namespaces, output_dir):
    # XXX programmatic instead?

    input_paths = ":".join(input_paths)
    input_namespaces = " ".join(input_namespaces)

    make_dirs(output_dir)

    options = list()
    options.append("--graph all")
    options.append("--html")
    options.append("--name \"{}\"".format(title))
    options.append("--no-private")
    options.append("--output {}".format(output_dir))
    options.append("--quiet")
    options.append("--url \"@site-url@/index.html\"")
    options = " ".join(options)

    call("PYTHONPATH={} epydoc {} {}", input_paths, options, input_namespaces)

    touch(join(output_dir, ".transom-skip"))

def gen_rdoc(release, title, base_input_path, input_paths, output_dir):
    output_dir = os.path.abspath(output_dir)

    # rdoc really wants to make the last dir
    make_dirs(split(output_dir)[0])

    options = list()
    options.append("--fmt html")
    options.append("--op {}".format(output_dir))
    options.append("--quiet")
    options.append("--title \"{}\"".format(title))
    options = " ".join(options)

    input_paths = " ".join(input_paths)

    call("cd {} && rdoc {} {}", base_input_path, options, input_paths)
    
    touch(join(output_dir, ".transom-skip"))
