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
  || *Issues* || [Completed features](https://issues.apache.org/jira/issues/?jql=project+%3D+%22Qpid%22+and+issuetype+%3D+%22New+Feature%22+and+status+in+%28%22Closed%22%2C+%22Resolved%22%29+and+resolution+%3D+%22Fixed%22+and+component+%3D+%22C%2B%2B+Broker%22) ||

## Features

<div class="two-column" markdown="1">
 - Speaks and translates between AMQP 1.0 and 0-10
 - [Management](@current-release-url@/cpp-broker/book/chapter-Managing-CPP-Broker.html#section-Managing-CPP-Broker) via [QMF](@site-url@/components/qmf/index.html)
 - Access control lists
 - [Federation](@current-release-url@/cpp-broker/book/chap-Messaging_User_Guide-Broker_Federation.html)
 - Flexible logging
 - Header-based routing
 - Heartbeats
 - [High availability](@current-release-url@/cpp-broker/book/chapter-ha.html)
 - [Message groups](@current-release-url@/cpp-broker/book/Using-message-groups.html)
 - Message TTLs and arrival timestamps
 - Pluggable persistence
 - [Pluggable authentication via SASL](@current-release-url@/cpp-broker/book/chap-Messaging_User_Guide-Security.html)
 - [Producer flow control](@current-release-url@/cpp-broker/book/producer-flow-control.html)
 - [Queue replication](@current-release-url@/cpp-broker/book/ha-queue-replication.html)
 - Resource limits
 - Secure connection via SSL
 - [Server-side selectors](https://issues.apache.org/jira/browse/QPID-4558?focusedCommentId=13592659&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-13592659)
 - Specialized queueing with [last value queue](@current-release-url@/cpp-broker/book/ch01s06.html), priority queue, and ring queue
 - [Threshold alerts](https://issues.apache.org/jira/browse/QPID-3002)
 - Transactions
 - Undeliverable message handling
</div>

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases](@site-url@/releases/index.html#past-releases).

 - [C++ broker book](@current-release-url@/cpp-broker/book/index.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/tags/@current-release@/qpid/cpp/INSTALL)
