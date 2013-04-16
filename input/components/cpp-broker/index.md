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
 - [Management](@current-release-url@/cpp-broker/book/html/index.html#section-Managing-CPP-Broker) via [QMF](@site-url@/components/qmf/index.html)
 - [Access control lists](@current-release-url@/cpp-broker/book/html/index.html#sect-Messaging_User_Guide-Security-Authorization)
 - [Federation](@current-release-url@/cpp-broker/book/html/index.html#chap-Messaging_User_Guide-Broker_Federation)
 - Flexible logging
 - Header-based routing
 - Heartbeats
 - [High availability](@current-release-url@/cpp-broker/book/html/index.html#chap-Messaging_User_Guide-Active_Passive_Cluster)
 - Pluggable persistence
 - [Pluggable authentication via SASL](@current-release-url@/cpp-broker/book/html/index.html#chap-Messaging_User_Guide-Security)
 - [Producer flow control](@current-release-url@/cpp-broker/book/html/index.html#producer-flow-control)
 - [Queue replication](@current-release-url@/cpp-broker/book/html/index.html#queue-state-replication)
 - [Resource limits](@current-release-url@/cpp-broker/book/html/index.html#sect-Messaging_User_Guide-Authorization-Specifying_ACL_Quotas)
 - [Secure connection via SSL](@current-release-url@/cpp-broker/book/html/index.html#sect-Messaging_User_Guide-Security-Encryption_using_SSL)
 - Specialized queueing with [last value queue](@current-release-url@/cpp-broker/book/html/index.html#idp3648256), [message groups](@current-release-url@/cpp-broker/book/html/index.html#Using-message-groups), priority queue, and ring queue
 - [Threshold alerts](https://issues.apache.org/jira/browse/QPID-3002)
 - Transactions
</div>

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases](@site-url@/releases/index.html#past-releases).

 - [C++ broker book](@current-release-url@/cpp-broker/book/html/index.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/tags/@current-release@/qpid/cpp/INSTALL)
