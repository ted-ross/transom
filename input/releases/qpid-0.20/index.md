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

# Qpid 0.20

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, C#, JMS, Perl,
Python, and Ruby.  More about [Qpid](@site-url@/index.html).

## Changes

 - [Release notes](release-notes.html)

## Downloads

It's important to [verify the
integrity](@site-url@/download.html#verify-what-you-download) of the
files you download.

  || *Content* || *Download* || *Signature* ||
  || Full source || [qpid-0.20.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.20/qpid-0.20.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.20/qpid-0.20.tar.gz.asc) ||
  || C++ broker, Qpid Messaging API (C++, bindings) || [qpid-cpp-0.20.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.20/qpid-cpp-0.20.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.20/qpid-cpp-0.20.tar.gz.asc) ||
  || C++ broker command-line tools || [qpid-tools-0.20.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.20/qpid-tools-0.20.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.20/qpid-tools-0.20.tar.gz.asc) ||
  || Java broker || [qpid-java-broker-0.20.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.20/qpid-java-broker-0.20.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.20/qpid-java-broker-0.20.tar.gz.asc) ||
  || Qpid JMS (AMQP 0-10, 0-91, 0-9, 0-8) || [qpid-java-client-0.20.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.20/qpid-java-client-0.20.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.20/qpid-java-client-0.20.tar.gz.asc) ||
  || Qpid JMS (AMQP 1.0) || [qpid-java-amqp-1-0-client-jms-0.20.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.20/qpid-java-amqp-1-0-client-jms-0.20.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.20/qpid-java-amqp-1-0-client-jms-0.20.tar.gz.asc) ||
  || Qpid Messaging API (Python) || [qpid-python-0.20.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.20/qpid-python-0.20.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.20/qpid-python-0.20.tar.gz.asc) ||
  || Qpid WCF || [qpid-wcf-0.20.zip](http://www.apache.org/dyn/closer.cgi/qpid/0.20/qpid-wcf-0.20.zip) || [PGP](http://www.apache.org/dist/qpid/0.20/qpid-wcf-0.20.zip.asc) ||
  || QMF || [qpid-qmf-0.20.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/0.20/qpid-qmf-0.20.tar.gz) || [PGP](http://www.apache.org/dist/qpid/0.20/qpid-qmf-0.20.tar.gz.asc) ||

Java artefacts are released as compiled bytecode.  Source code is
available in the full source artefact.

## Components

  || *Component* || *Languages* || *Platforms* || *AMQP versions* ||
  || [C++ broker](@site-url@/components/cpp-broker/index.html) || C++ || Linux, Windows || 1.0, 0-10 ||
  || [Java broker](@site-url@/components/java-broker/index.html) || Java || JVM || 1.0, 0-10, 0-91, 0-9, 0-8 ||
  || [Qpid JMS](@site-url@/components/qpid-jms/index.html) || Java || JVM || 1.0, 0-10, 0-91, 0-9, 0-8 ||
  || [Qpid Messaging API](@site-url@/components/messaging-api/index.html) || C++, Perl, Python, Ruby, .NET || Linux, Windows || 1.0, 0-10 ||
  || [Qpid WCF](@site-url@/components/qpid-wcf/index.html) || C# || Windows || 0-10 ||
  || [QMF](@site-url@/components/qmf/index.html) || C++, Python || Linux || 0-10 ||

## Documentation

 - [Programming in Apache Qpid](http://qpid.apache.org/books/0.20/Programming-In-Apache-Qpid/html/index.html)
 - [Guide to the C++ broker](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/index.html)
 - [Guide to the Java broker](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-Java-Book/html/index.html)
 - [Installing and Using Qpid Java](https://cwiki.apache.org/qpid/getting-started-guide.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/tags/0.20/qpid/cpp/INSTALL)
 - [Installing Qpid Python](http://svn.apache.org/repos/asf/qpid/tags/0.20/qpid/python/README.txt)
 - [Installing Qpid WCF](http://svn.apache.org/repos/asf/qpid/tags/0.20/qpid/wcf/ReadMe.txt)

### API reference

 - [C++ Messaging API](messaging-api/cpp/api/index.html)
 - [Python Messaging API](messaging-api/python/api/index.html)
 - [Ruby Messaging API](messaging-api/ruby/api/index.html)
 - [.NET Messaging API](messaging-api/dotnet/api/index.html)

## More information

 - [All release artefacts](http://www.apache.org/dyn/closer.cgi/qpid/0.20)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+QPID+AND+fixVersion+in+%28%270.19%27%2C+%270.20%27%29+ORDER+BY+priority+DESC)
 - [Source repository branch](http://svn.apache.org/repos/asf/qpid/branches/0.20)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/tags/0.20)
