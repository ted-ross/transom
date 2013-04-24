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

from __future__ import print_function

import atexit
import codecs
import fnmatch
import getpass
import os
import shutil
import subprocess
import sys
import tempfile

# The notion here is to use the global function namespace for common
# script operations.  They fall into a few patterns:
# 
# - split and join are path operations
#
# - "path" param means path to a file 
# - "dir" param means path to a directory
# - "name" param means the file or directory name without any
#   preceding path
# - "pattern" param means a shell glob, a la "*.py"
#
# - read_, write_, append_, and touch_entry are for stashing named
#   values in the a temporary location in the filesystem, to make it
#   easy to use those values when you invoke an external command
#
# - If the function involves creating a file or directory, it may well
#   return the path

def error(message, *args):
    _print("Error", message, args, sys.stderr)

    raise Exception()

def warn(message, *args):
    _print("Warn", message, args, sys.stderr)

def notice(message, *args):
    _print(None, message, args, sys.stdout)

def debug(message, *args):
    pass

def _print(category, message, args, file):
    if category:
        message = "{}: {}".format(category, message)

    if args:
        message = message.format(*args)

    print(message, file=file)

join = os.path.join
split = os.path.split
exists = os.path.exists
is_dir = os.path.isdir
is_file = os.path.isfile

def read(path):
    with codecs.open(path, encoding="utf-8", mode="r") as file:
        return file.read()

def write(path, string):
    with codecs.open(path, encoding="utf-8", mode="w") as file:
        file.write(string)

    return path

def append(path, string):
    with codecs.open(path, encoding="utf-8", mode="a") as file:
        file.write(string)

    return path

def prepend(path, string):
    orig = read(path)
    prepended = string + orig
    write(path, prepended)

    return path

def touch(path):
    return append(path, "")

_entry_dir = tempfile.mkdtemp()

def _remove_entry_dir():
    remove(_entry_dir)

atexit.register(_remove_entry_dir)

def read_entry(key):
    return read(join(_entry_dir, key))

def write_entry(key, string):
    path = get_entry_path(key)
    write(path, string)
    return path

def append_entry(key, string):
    path = get_entry_path(key)
    append(path, string)
    return path

def touch_entry(key):
    return append_entry(key, "")

def get_entry_path(key):
    return join(_entry_dir, key)

def copy(from_path, to_path):
    to_dir = split(to_path)[0]

    if to_dir:
        make_dirs(to_dir)

    if is_dir(from_path):
        shutil.copytree(from_path, to_path)
    else:
        shutil.copy(from_path, to_path)

move = shutil.move

def remove(path):
    if not exists(path):
        return

    if is_dir(path):
        shutil.rmtree(path, ignore_errors=True)
    else:
        os.remove(path)

def find(dir, *patterns):
    matched_paths = set()

    if not patterns:
        patterns = ("*",)

    for root, dirs, files in os.walk(dir):
        for pattern in patterns:
            matched_dirs = fnmatch.filter(dirs, pattern)
            matched_files = fnmatch.filter(files, pattern)

            matched_paths.update([join(root, x) for x in matched_dirs])
            matched_paths.update([join(root, x) for x in matched_files])

    return sorted(matched_paths)

def list_dir(dir, *patterns):
    names = os.listdir(dir)

    if not patterns:
        return sorted(names)

    matched_names = set()

    for pattern in patterns:
        matched_names.update(fnmatch.filter(names, pattern))

    return sorted(matched_names)

def make_dirs(dir):
    if not exists(dir):
        os.makedirs(dir)

    return dir

def make_temp_dir():
    return tempfile.mkdtemp()

def make_user_temp_dir():
    temp_dir = tempfile.gettempdir()
    user = getpass.getuser()
    user_temp_dir = join(temp_dir, user)

    return make_dirs(user_temp_dir)

def call(command, *args):
    if args:
        command = command.format(*args)

    notice("Calling '{}'", command)

    subprocess.check_call(command, shell=True)

def make_archive(input_dir, output_dir, output_name, format="gztar"):
    temp_dir = make_temp_dir()
    temp_input_dir = join(temp_dir, output_name)

    copy(input_dir, temp_input_dir)

    base_output_path = join(output_dir, output_name)

    return shutil.make_archive(base_name=base_output_path,
                               format=format,
                               root_dir=temp_dir,
                               base_dir=output_name)

### Less generic functions ###

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
