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

# C++ Broker

A message broker written in C++ that stores, routes, and forwards
messages using AMQP.

  || *Platforms* || Linux, Windows ||
  || *AMQP versions* || 1.0, 0-10 ||
  || *Download* || [qpid-cpp-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-cpp-@current-release@.tar.gz) \[[PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-cpp-@current-release@.tar.gz.asc)] ||
  || *Source location* ||  <http://svn.apache.org/repos/asf/qpid/trunk/qpid/cpp/> ||

## Features

<div class="two-column" markdown="1">
 - [Management](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/chapter-Managing-CPP-Broker.html#section-Managing-CPP-Broker) via [QMF](@site-url@/components/qmf/index.html)
 - [Access control lists](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/chap-Messaging_User_Guide-Security.html#sect-Messaging_User_Guide-Security-Authorization)
 - [Federation](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/chap-Messaging_User_Guide-Broker_Federation.html)
 - Header-based routing
 - Heartbeats
 - [High availability](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/chap-Messaging_User_Guide-Active_Passive_Cluster.html)
 - Pluggable persistence
 - [Pluggable authentication via SASL](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/chap-Messaging_User_Guide-Security.html)
 - [Producer flow control](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/producer-flow-control.html)
 - [Queue replication](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/ch01s14.html)
 - [Resource limits](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/chap-Messaging_User_Guide-Security.html#sect-Messaging_User_Guide-Authorization-Specifying_ACL_Quotas)
 - [Secure connection via SSL](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/chap-Messaging_User_Guide-Security.html#sect-Messaging_User_Guide-Security-Encryption_using_SSL)
 - Specialized queueing
   - Last value queue
   - [Message groups](http://qpid.apache.org/books/0.20/AMQP-Messaging-Broker-CPP-Book/html/Using-message-groups.html)
   - Ring queue
 - Threshold alerts
 - Transactions
</div>

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases](@site-url@/releases/index.html#past-releases).

 - [Guide to the C++ broker](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-CPP-Book/html/index.html) ([PDF](http://qpid.apache.org/books/@current-release@/AMQP-Messaging-Broker-CPP-Book/pdf/AMQP-Messaging-Broker-CPP-Book.pdf))
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/tags/@current-release@/qpid/cpp/INSTALL)
