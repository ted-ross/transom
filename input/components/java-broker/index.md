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

## Features

 - JMS 1.1 compliant
 - Speaks and translates among all versions of AMQP
 - [Management via JMX, REST, QMF, and web console](http://qpid.apache.org/books/trunk/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Configuring-And-Managing.html)
 - [Access control lists](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Security-ACLs.html)
 - [Flexible logging](https://cwiki.apache.org/qpid/configure-operational-status-logging.html)
 - Flow to disk
 - Header-based routing
 - [Heartbeats](https://cwiki.apache.org/qpid/configure-broker-and-client-heartbeating.html)
 - [High availability](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-High-Availability.html)
 - Message groups
 - Pluggable persistence
   - [Derby store](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Stores-Derby-Store.html)
   - [BDB store](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Stores-BDB-Store.html)
   - [High-availability BDB store](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Stores-HA-BDB-Store.html)
 - Pluggable authentication
   - [LDAP](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Security-Authentication-Providers.html#LDAPAuthManager)
   - [Kerberos](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Security-Authentication-Providers.html#id2497060)
   - [SSL client certificates](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Security-Authentication-Providers.html#ExternalAuthManager)
 - [Producer flow control](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Runtime-Disk-Space-Management.html#Qpid-Producer-Flow-Control)
 - [Secure connection via SSL](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Security-SSL.html)
 - Server-side selectors
 - Specialized queuing
   - [Last value queue](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Queues-OtherTypes.html#Java-Broker-Queues-OtherTypes-LVQ)
   - [Priority queue](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Queues-OtherTypes.html#Java-Broker-Queues-OtherTypes-Priority)
   - [Sorted queue](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/Java-Broker-Queues-OtherTypes.html#Java-Broker-Queues-OtherTypes-Sorted)
 - Threshold alerts
 - Transactions
 - [Virtual hosts](https://cwiki.apache.org/qpid/configure-the-virtual-hosts-via-virtualhostsxml.html)

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases](@site-url@/releases/index.html#past-releases).

 - [Guide to the Java broker](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/html/index.html) ([PDF](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-Java-Book/pdf/AMQP-Messaging-Broker-Java-Book.pdf))
 - [How to build Qpid Java](https://cwiki.apache.org/qpid/qpid-java-build-how-to.html)
 - [Installing and Using Qpid Java](https://cwiki.apache.org/qpid/getting-started-guide.html)
 - [FAQ](https://cwiki.apache.org/qpid/qpid-java-faq.html)
 - [Troubleshooting guide](https://cwiki.apache.org/qpid/qpid-troubleshooting-guide.html)
 - [Design documents](https://cwiki.apache.org/qpid/java-broker-design.html)
 - [More documents on the wiki](https://cwiki.apache.org/qpid/qpid-java-documentation.html)
