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

import os
import re
import shutil
import string
import sys

from collections import defaultdict
from pprint import pprint

class TransomError(Exception):
    pass

def error(message, *args):
    _print("Error", message, args, sys.stderr)

    raise TransomError()

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
