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

# Qpid 0.14

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, C#, JMS, Perl,
Python, and Ruby.  More about [Qpid](@site-url@/index.html).

## Changes

 - [Release notes](release-notes.html)

## Components

  || *Component* || *Platforms* || *AMQP versions* ||
  || [C++ broker](@site-url@/components/cpp-broker/index.html) || Linux, Windows || 0-10 ||
  || [Java broker](@site-url@/components/java-broker/index.html) || JVM || 0-10, 0-91, 0-9, 0-8 ||
  || [Qpid JMS](@site-url@/components/qpid-jms/index.html) || JVM || 0-10, 0-91, 0-9, 0-8 ||
  || [Qpid Messaging API](@site-url@/components/messaging-api/index.html) || Linux, Windows || 0-10 ||
  || [Qpid WCF](@site-url@/components/qpid-wcf/index.html) || Windows || 0-10 ||
  || [QMF](@site-url@/components/qmf/index.html) || Linux || 0-10 ||

## Downloads

It's important to [verify the
integrity](@site-url@/download.html#verify-what-you-download) of the
files you download.

  || *Content* || *Download* || *Signature* ||
  || Full source || [qpid-0.14.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.14/qpid-0.14.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.14/qpid-0.14.tar.gz.asc) ||
  || C++ broker and Messaging API || [qpid-cpp-0.14.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.14/qpid-cpp-0.14.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.14/qpid-cpp-0.14.tar.gz.asc) ||
  || C++ broker command-line tools || [qpid-tools-0.14.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.14/qpid-tools-0.14.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.14/qpid-tools-0.14.tar.gz.asc) ||
  || Java broker, Qpid JMS, and tools || [qpid-java-0.14.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.14/qpid-java-0.14.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.14/qpid-java-0.14.tar.gz.asc) ||
  || Java broker || [qpid-java-broker-0.14.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.14/qpid-java-broker-0.14.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.14/qpid-java-broker-0.14.tar.gz.asc) ||
  || Qpid JMS || [qpid-java-client-0.14.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.14/qpid-java-client-0.14.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.14/qpid-java-client-0.14.tar.gz.asc) ||
  || Python Messaging API || [qpid-python-0.14.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.14/qpid-python-0.14.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.14/qpid-python-0.14.tar.gz.asc) ||
  || Qpid WCF || [qpid-wcf-0.14.zip](http://www.apache.org/dyn/closer.cgi/qpid/0.14/qpid-wcf-0.14.zip) || [PGP](http://www.apache.org/dist/qpid/0.14/qpid-wcf-0.14.zip.asc) ||
  || QMF || [qpid-qmf-0.14.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.14/qpid-qmf-0.14.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.14/qpid-qmf-0.14.tar.gz.asc) ||

## Documentation

 - [Programming in Apache Qpid](http://qpid.apache.org/books/0.14/Programming-In-Apache-Qpid/html/index.html) ([PDF](http://qpid.apache.org/books/0.14/Programming-In-Apache-Qpid/pdf/Programming-In-Apache-Qpid.pdf))
 - [Guide to the C++ broker](http://qpid.apache.org/books/0.14/AMQP-Messaging-Broker-CPP-Book/html/index.html) ([PDF](http://qpid.apache.org/books/0.14/AMQP-Messaging-Broker-CPP-Book/pdf/AMQP-Messaging-Broker-CPP-Book.pdf))
 - [Guide to the Java broker](http://qpid.apache.org/books/0.14/AMQP-Messaging-Broker-Java-Book/html/index.html) ([PDF](http://qpid.apache.org/books/0.14/AMQP-Messaging-Broker-Java-Book/pdf/AMQP-Messaging-Broker-Java-Book.pdf))
 - [Installing and Using Qpid Java](https://cwiki.apache.org/qpid/getting-started-guide.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/tags/0.14/qpid/cpp/INSTALL)
 - [Installing Qpid Python](http://svn.apache.org/repos/asf/qpid/tags/0.14/qpid/python/README.txt)
 - [Installing Qpid WCF](http://svn.apache.org/repos/asf/qpid/tags/0.14/qpid/wcf/ReadMe.txt)
 - [C++ Messaging API reference](http://qpid.apache.org/apis/0.14/cpp/html/index.html) ([qpid-cpp-doxygen-0.14.html.tar.gz](http://qpid.apache.org/apis/0.14/cpp/qpid-cpp-doxygen-0.14.html.tar.gz))
 - [Python Messaging API reference](http://qpid.apache.org/apis/0.14/python/html/index.html) ([qpid-python-epydoc-0.14.html.tar.gz](http://qpid.apache.org/apis/0.14/python/qpid-python-epydoc-0.14.html.tar.gz))

## More information

 - [All release artefacts](http://www.apache.org/dyn/closer.cgi/qpid/0.14)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+in+%28%270.13%27%2C+%270.14%27%29+ORDER+BY+priority+DESC)
 - [Source repository branch](https://svn.apache.org/repos/asf/qpid/branches/0.14)
 - [Source repository tag](https://svn.apache.org/repos/asf/qpid/tags/0.14)
