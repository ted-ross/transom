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

# Java Broker

A message broker written in Java that stores, routes, and forwards
messages using AMQP.

  || *Platforms* || JVM ||
  || *AMQP versions* || 1.0, 0-10, 0-91, 0-9, 0-8 ||
  || *Download* || [qpid-java-broker-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-java-broker-@current-release@.tar.gz) \[[PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-java-broker-@current-release@.tar.gz.asc)] ||
  || *Source location* ||  <http://svn.apache.org/repos/asf/qpid/trunk/qpid/java/> ||
  || *Issues* || [Completed features](https://issues.apache.org/jira/issues/?jql=project+%3D+%22Qpid%22+and+issuetype+%3D+%22New+Feature%22+and+status+in+%28%22Closed%22%2C+%22Resolved%22%29+and+resolution+%3D+%22Fixed%22+and+component+%3D+%22Java+Broker%22) ||

## Features

<div class="two-column" markdown="1">
 - JMS 1.1 compliant
 - Speaks and translates among all versions of AMQP
 - [Management](@current-release-url@/java-broker/book/Java-Broker-Configuring-And-Managing.html) via JMX, REST, QMF, and web console
 - [Access control lists](@current-release-url@/java-broker/book/Java-Broker-Security-ACLs.html)
 - Flexible logging
 - Flow to disk
 - Header-based routing
 - Heartbeats
 - [High availability](@current-release-url@/java-broker/book/Java-Broker-High-Availability.html)
 - Message groups
 - [Pluggable persistence](@current-release-url@/java-broker/book/Java-Broker-Stores.html) supporting Derby, SQL, and BDB stores
 - [Pluggable authentication](@current-release-url@/java-broker/book/Java-Broker-Security-Authentication-Providers.html) supporting LDAP, Kerberos, and SSL client certificates
 - [Producer flow control](@current-release-url@/java-broker/book/Qpid-Producer-Flow-Control.html)
 - [Secure connection via SSL](@current-release-url@/java-broker/book/Java-Broker-Security-SSL.html)
 - Server-side selectors
 - [Specialized queuing](@current-release-url@/java-broker/book/Java-Broker-Queues.html) with last value queue, priority queue, and sorted queue
 - Threshold alerts
 - Transactions
 - [Undeliverable message handling](@current-release-url@/java-broker/book/Java-Broker-Runtime-Handling-Undeliverable-Messages.html)
 - [Virtual hosts](@current-release-url@/java-broker/book/Java-Broker-Virtual-Hosts.html)
</div>

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases](@site-url@/releases/index.html#past-releases).

 - [Java broker book](@current-release-url@/java-broker/book/index.html)
 - [How to build Qpid Java](https://cwiki.apache.org/qpid/qpid-java-build-how-to.html)
 - [Installing and Using Qpid Java](https://cwiki.apache.org/qpid/getting-started-guide.html)
 - [FAQ](https://cwiki.apache.org/qpid/qpid-java-faq.html)
 - [Troubleshooting guide](https://cwiki.apache.org/qpid/qpid-troubleshooting-guide.html)
 - [Design documents](https://cwiki.apache.org/qpid/java-broker-design.html)
 - [More documents on the wiki](https://cwiki.apache.org/qpid/qpid-java-documentation.html)
