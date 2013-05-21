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

# Components

Qpid offers these tools to help you build AMQP-based distributed
applications.

## Messaging APIs

Qpid's messaging APIs can help you make your application speak AMQP.

 - [AMQP Messenger](messenger/index.html) - Forget plumbing and focus on your task
 - [AMQP Protocol Engine](protocol-engine/index.html) - Fine-grained control over AMQP 1.0
 - [Qpid JCA](qpid-jca/index.html) - A JCA resource adapter for AMQP brokers
 - [Qpid JMS](qpid-jms/index.html) - An AMQP-fluent [Java Message Service](http://en.wikipedia.org/wiki/Java_Message_Service) implementation
 - [Qpid Messaging API](messaging-api/index.html) - A connection-oriented messaging API that supports many languages
 - [Qpid WCF](qpid-wcf/index.html) - An AMQP [Windows Communication Foundation](http://msdn.microsoft.com/en-us/library/ms731082.aspx) implementation

## Servers and tools

Use these components to build a messaging fabric for any AMQP
application.

Qpid's message brokers are full-featured [message-oriented
middleware](http://en.wikipedia.org/wiki/Message-oriented_middleware)
brokers.  They offer specialized queueing behaviors, message
persistence, and manageability.

 - [C++ broker](cpp-broker/index.html) - A native-code AMQP message broker
 - [C++ broker command-line tools](cpp-broker-tools/index.html) - Manage the C++ broker
 - [Java broker](java-broker/index.html) - A pure-Java AMQP message broker
 - [QMF](qmf/index.html) - Management built on Qpid messaging

;; ## Servers

;; Messaging architectures use reliable intermediaries (usually network
;; servers) to decouple the parts of a distributed application so that
;; each part can operate independently and the system as a whole can
;; tolerate failures.

;; ### Routers, proxies, bridges, and more

;; Traditional message brokers aren't the only kind of intermediary in an
;; AMQP ecosystem.  The future of messaging offers a wide variety of
;; architecture components to support robust internet-wide distributed
;; applications.  The Qpid community is right now building the
;; foundations for these new technologies.

## Deprecated components

The following components are no longer supported.

 - The `qpid::client` API, replaced by the [Qpid Messaging API](messaging-api/index.html)
 - The `qpid::management` API, replaced by [QMF](qmf/index.html)
