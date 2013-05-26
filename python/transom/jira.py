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

import copy
import os
import sqlite3
import urllib

from xml.etree.ElementTree import *

class IssueDatabase(object):
    def __init__(self, path):
        self.path = path

    def init(self):
        columns = list()

        for name in _Record._fields:
            field_type = _Record._field_types.get(name, unicode)
            column_type = "text"

            if field_type == int:
                column_type = "integer"

            column = "%s %s" % (name, column_type)

            columns.append(column)

        ddl = "create table issues (%s)" % ", ".join(columns)
        conn = sqlite3.connect(self.path)
        
        try:
            cursor = conn.cursor()
            cursor.execute(ddl)
        finally:
            conn.close()

    def update(self, xml_path):
        file = open(xml_path)

        try:
            tree = ElementTree()
            tree.parse(file)
        finally:
            file.close()

        root = tree.getroot()
        channel = root.find("channel")

        conn = sqlite3.connect(self.path)

        try:
            cursor = conn.cursor()

            for elem in channel.findall("item"):
                record = _Record()
                record.parse(elem)
                record.insert(cursor)

                conn.commit()
        finally:
            conn.close()

    def clear(self):
        if os.path.exists(self.path):
            os.remove(self.path)

class _Record(object):
    _fields = {
        "key": "key/#",
        "component": "component/#",
        "version": "version/#",
        "summary": "summary/#",
        "link": "link/#",
        "fix_version": "fixVersion/#",
        "type_id": "type/@id",
        "type": "type/#",
        "assignee_username": "assignee/@username",
        "assignee": "assignee/#",
        "reporter_username": "reporter/@username",
        "reporter": "reporter/#",
        "status_id": "status/@id",
        "status": "status/#",
        "priority_id": "priority/@id",
        "priority": "priority/#",
        "resolution_id": "resolution/@id",
        "resolution": "resolution/#",
        }

    _field_types = {
        "type_id": int,
        "status_id": int,
        "priority_id": int,
        "resolution_id": int,
        }

    def __init__(self):
        for name in self._fields:
            setattr(self, name, None)

    def parse(self, elem):
        for name in self._fields:
            value = self.get_value(elem, self._fields[name])

            field_type = self._field_types.get(name, unicode)

            if value is not None:
                value = field_type(value)

            setattr(self, name, value)

    def get_value(self, elem, path):
        tokens = path.split("/")
        child = elem

        for token in tokens:
            if child is None:
                return

            if token == "#":
                return child.text

            if token.startswith("@"):
                return child.attrib[token[1:]]
            
            child = child.find(token)

    def insert(self, cursor):
        fields = sorted(self._fields)
        columns = ", ".join(fields)
        values = ", ".join("?" * len(fields))
        args = [getattr(self, x) for x in fields]

        dml = "insert into issues (%s) values (%s)" % (columns, values)

        #print dml, args

        cursor.execute(dml, args)

class Query(object):
    statuses = (
        "Open",
        "Closed",
        "Reopened",
        "In Progress",
        "Ready To Review",
        "Resolved",
        )

    resolutions = (
        "Fixed",
        "Won't Fix",
        "Duplicate",
        "Invalid",
        "Incomplete",
        "Cannot Reproduce",
        "Later",
        "Not A Problem",
        "Unresolved",
        "Implemented",
        )

    def __init__(self):
        self.base_url = "https://issues.apache.org/jira/issues/"
        self.exprs = list()

    def copy(self):
        other = Query()
        other.exprs = copy.copy(self.exprs)
        return other

    def add(self, name, operator, value):
        if operator in ("=", "!=", "~"):
            value = "\"{}\"".format(value)

        self.exprs.append((name, operator, value))

    def render(self):
        exprs = ["{} {} {}".format(*x) for x in self.exprs]
        jql = " and ".join(exprs)
        jql = urllib.quote_plus(jql)

        return "{}?jql={}".format(self.base_url, jql)

class QpidQuery(Query):
    project = "Qpid"

    components = (
        "Build Tools",
        "C++ Broker",
        "C++ Client",
        "C++ Clustering",
        "Documentation",
        "Dot Net Client",
        "Interop Testing",
        "Java Broker",
        "Java Client",
        "Java Common",
        "Java Management : JMX Console",
        "Java Performance Tests",
        "Java Tests",
        "Java Tools",
        "JCA",
        "Packaging",
        "Perl Client",
        "Proton",
        "Python Client",
        "Python Test Suite",
        "Python Tools",
        "Qpid Dispatch",
        "Qpid Examples",
        "Qpid Management Framework",
        "Ruby Client",
        "Tools",
        "WCF/C++ Client",
        "Website",
        )

    versions = (
        "0.23",
        "0.22",
        "0.21",
        "0.20",
        "0.19",
        "0.18",
        "0.17",
        "0.16",
        "0.15",
        "0.14",
        "0.13",
        "0.12",
        "0.11",
        "0.10",
        "0.9",
        "0.8",
        "0.7",
        "0.6",
        "0.5",
        "M4",
        "M3",
        "M2.1",
        "M2",
        "M1",
        "JIRA Cleanup",
        "Future",
        )

    committers = (
        "Alan Conway",
        "Alex Rudyy",
        "Andrew Stitcher",
        "Chuck Rolke",
        "Cliff Jansen",
        "Darryl L. Pierce",
        "Fraser Adams",
        "Gordon Sim",
        "Justin Ross",
        "Keith Wall",
        "Ken Giusti",
        "Kim van der Riet",
        "michael j. goulish",
        "Philip Harvey",
        "Rafael H. Schloming",
        "Rajith Attapattu",
        "Rob Godfrey",
        "Robbie Gemmell",
        "Steve Huston",
        "Ted Ross",
        "Weston M. Price",
        )

    def __init__(self):
        super(QpidQuery, self).__init__()

        self.add("project", "=", self.project)
