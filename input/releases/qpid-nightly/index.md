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

# Qpid Nightly

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, Java, Perl,
Python, Ruby, and .NET.  More about [Qpid](@site-url@/index.html).

## Downloads

  || *Content* || *Download* ||
  || Full source || [qpid-nightly.tar.gz]()) ||
  || C++ broker, Qpid Messaging API (C++, bindings) || [qpid-cpp-nightly.tar.gz]() ||
  || C++ broker command-line tools || [qpid-tools-nightly.tar.gz]() ||
  || Java broker, Qpid JCA || [qpid-java-broker-nightly.tar.gz]() ||
  || Qpid JMS (AMQP 0-10, 0-91, 0-9, 0-8) || [qpid-java-client-nightly.tar.gz]() ||
  || Qpid JMS (AMQP 1.0) || [qpid-java-amqp-1-0-client-jms-nightly.tar.gz]() ||
  || Qpid Messaging API (Python) || [qpid-python-nightly.tar.gz]() ||
  || Qpid WCF || [qpid-wcf-nightly.zip]() ||
  || QMF || [qpid-qmf-nightly.tar.gz]() ||

Java artefacts are released as compiled bytecode.  Source code is
available in the full source artefact.

## Components

  || *Component* || *Languages* || *Platforms* || *AMQP versions* ||
  || [C++ broker](@site-url@/components/cpp-broker/index.html) || C++ || Linux, Windows || 1.0, 0-10 ||
  || [C++ broker command-line tools](@site-url@/components/cpp-broker-tools/index.html) || - || Linux || 0-10 ||
  || [Java broker](@site-url@/components/java-broker/index.html) || Java || JVM || 1.0, 0-10, 0-91, 0-9, 0-8 ||
  || [Qpid JCA](@site-url@/components/qpid-jca/index.html) || Java || JVM || 0-10 ||
  || [Qpid JMS](@site-url@/components/qpid-jms/index.html) || Java || JVM || 1.0, 0-10, 0-91, 0-9, 0-8 ||
  || [Qpid Messaging API](@site-url@/components/messaging-api/index.html) || C++, Perl, Python, Ruby, .NET || Linux, Windows || 1.0, 0-10 ||
  || [Qpid WCF](@site-url@/components/qpid-wcf/index.html) || .NET || Windows || 0-10 ||
  || [QMF](@site-url@/components/qmf/index.html) || C++, Python || Linux || 0-10 ||

## Documentation

<div class="three-column" markdown="1">

### Installation

 - [Installing and Using Qpid Java](https://cwiki.apache.org/qpid/getting-started-guide.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/trunk/qpid/cpp/INSTALL)
 - [Installing Qpid Python](http://svn.apache.org/repos/asf/qpid/trunk/qpid/python/README.txt)

### C++ Broker

 - [C++ broker book]() ([PDF]())

### Java Broker

 - [Java broker book]() ([PDF]())

### QMF
 
 - [C++ API reference]()
 - [C++ examples]()
 - [Python examples]()
 - [Ruby examples]()

### Qpid JCA

 - [README](http://svn.apache.org/repos/asf/qpid/trunk/qpid/java/jca/README.txt)
 - [Examples](http://svn.apache.org/repos/asf/qpid/trunk/qpid/java/jca/example/)

### Qpid JMS

 - [Using the Qpid JMS client]() ([PDF]())
 - [API reference](http://docs.oracle.com/javaee/1.4/api/javax/jms/package-summary.html)
 - [Examples]()

### Qpid Messaging API

 - [Using the Qpid Messaging API]() ([PDF]())
 - [The .NET Binding for the C++ Messaging Client]()
 - [.NET API reference]()
 - [.NET examples]()
 - [C++ API reference]()
 - [C++ examples]()
 - [Python API reference]()
 - [Python examples]()
 - [Ruby API reference]()
 - [Ruby examples]()

### Qpid WCF

 - [README](http://svn.apache.org/repos/asf/qpid/trunk/qpid/wcf/ReadMe.txt)
 - [Using the Qpid WCF client]() ([PDF]()
 - [API reference](http://msdn.microsoft.com/en-us/library/vstudio/ms735119\(v=vs.90\).aspx)
 - [Examples](http://svn.apache.org/repos/asf/qpid/trunk/qpid/wcf/samples)

</div>

## More information

 - [All release artefacts](http://www.apache.org/dist/qpid/nightly)
 - [Source repository](http://svn.apache.org/repos/asf/qpid/tunk)
