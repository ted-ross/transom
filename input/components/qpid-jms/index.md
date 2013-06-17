;;
;; Licensed to the Apache Software Foundation (ASF) under one
;; or more contributor license agreements.  See the NOTICE file
;; distributed with this work for additional information
;; regarding copyright ownership.  The ASF licenses this file
;; to you under the Apache License, Version 2.0 (the
;; "License"); you may not use this file except in compliance
;; with the License.  You may obtain a copy of the License at
;; 
;;   http://www.apache.org/licenses/LICENSE-2.0
;; 
;; Unless required by applicable law or agreed to in writing,
;; software distributed under the License is distributed on an
;; "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
;; KIND, either express or implied.  See the License for the
;; specific language governing permissions and limitations
;; under the License.
;;

# Qpid JMS

A [Java Message
Service](http://en.wikipedia.org/wiki/Java_Message_Service) 1.1
implementation that speaks all versions of AMQP.

  || *Languages* || Java ||
  || *Platforms* || JVM ||
  || *AMQP versions* || 1.0\*, 0-10, 0-91, 0-9, 0-8 ||
  || *Downloads* || AMQP 0-10, 0-91, 0-9, 0-8: [qpid-java-client-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-java-client-@current-release@.tar.gz) \[[PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-java-client-@current-release@.tar.gz.asc)],<br/>AMQP 1.0: [qpid-java-amqp-1-0-client-jms-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-java-amqp-1-0-client-jms-@current-release@.tar.gz) \[[PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-java-amqp-1-0-client-jms-@current-release@.tar.gz.asc)] ||
  || *Source location* ||  <http://svn.apache.org/repos/asf/qpid/trunk/qpid/java/> ||
  || *Issues* || [Open bugs](https://issues.apache.org/jira/issues/?jql=project+%3D+%22Qpid%22+and+issuetype+%3D+%22Bug%22+and+status+in+%28%22Open%22%2C+%22Reopened%22%2C+%22In+Progress%22%2C+%22Ready+To+Review%22%29+and+component+%3D+%22Java+Client%22), [Completed enhancements](https://issues.apache.org/jira/issues/?jql=project+%3D+%22Qpid%22+and+issuetype+in+%28%22New+Feature%22%2C+%22Improvement%22%29+and+status+in+%28%22Closed%22%2C+%22Resolved%22%29+and+resolution+%3D+%22Fixed%22+and+component+%3D+%22Java+Client%22), [Requested enhancements](https://issues.apache.org/jira/issues/?jql=project+%3D+%22Qpid%22+and+issuetype+in+%28%22New+Feature%22%2C+%22Improvement%22%29+and+status+in+%28%22Open%22%2C+%22Reopened%22%2C+%22In+Progress%22%2C+%22Ready+To+Review%22%29+and+component+%3D+%22Java+Client%22) ||

\*1.0 support is offered in an implementation distinct from that of
older protocol versions.

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases](@site-url@/releases/index.html#past-releases).

 - [Using the Qpid JMS client](@current-release-url@/programming/book/QpidJMS.html)
 - [API reference](http://docs.oracle.com/javaee/1.4/api/javax/jms/package-summary.html)
 - [Examples](@current-release-url@/qpid-jms/examples/index.html)
 - [How to build Qpid Java](https://cwiki.apache.org/qpid/qpid-java-build-how-to.html)
 - [Installing and Using Qpid Java](https://cwiki.apache.org/qpid/getting-started-guide.html)
 - [Connection URL format](https://cwiki.apache.org/qpid/connection-url-format.html)
 - [Binding URL format](https://cwiki.apache.org/qpid/bindingurlformat.html)
 - [Client properties](https://cwiki.apache.org/qpid/system-properties.html#SystemProperties-ClientProperties)
 - [JNDI providers](https://cwiki.apache.org/qpid/using-qpid-with-other-jndi-providers.html)
