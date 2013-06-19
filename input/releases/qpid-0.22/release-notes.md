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

# Qpid 0.22 Release Notes

Qpid is a cross-platform AMQP messaging system.  It provides message
brokers written in C++ and Java, and clients for C++, Java, Perl,
Python, Ruby, and .NET.  More about [Qpid](@site-url@/index.html).

The full list of changes in the Qpid 0.22 release incorporates
both the issues worked on during the 0.21 development
stream and any final touches made during the 0.22 release
process. A list of these JIRA issues can be found below.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**Note:** This release addresses CVE-2013-1909. See
[QPID-4918](https://issues.apache.org/jira/browse/QPID-4918).

**Note:** The C++ broker clustering implementation has been replaced
by a new HA capability. See
[README-HA.txt](https://svn.apache.org/repos/asf/qpid/tags/0.22/qpid/cpp/README-HA.txt)
for information about how to migrate.

## New features and improvements

 - [QPID-3569](https://issues.apache.org/jira/browse/QPID-3569) - Refactor TransactionTimeout
 - [QPID-3833](https://issues.apache.org/jira/browse/QPID-3833) - Only string values for LVQ key are accepted
 - [QPID-4054](https://issues.apache.org/jira/browse/QPID-4054) - C++ Broker connection limits require better granularity
 - [QPID-4115](https://issues.apache.org/jira/browse/QPID-4115) - qpid-send and qpid-receive for Python client
 - [QPID-4116](https://issues.apache.org/jira/browse/QPID-4116) - Allow qpid-cpp-benchmark to run qpid-send and qpid-receive from specified directories
 - [QPID-4181](https://issues.apache.org/jira/browse/QPID-4181) - proton porting work on Windows
 - [QPID-4207](https://issues.apache.org/jira/browse/QPID-4207) - Installs the Swig .i files
 - [QPID-4318](https://issues.apache.org/jira/browse/QPID-4318) - QpidConnectionFactoryProxy should implement Queue/Topic Connection factory API's to support older clients
 - [QPID-4372](https://issues.apache.org/jira/browse/QPID-4372) - Have the C++ examples use CMake rather than static Makefiles.
 - [QPID-4390](https://issues.apache.org/jira/browse/QPID-4390) - Java Broker should allow runtime changes to persisted configuration
 - [QPID-4445](https://issues.apache.org/jira/browse/QPID-4445) - publish the JCA module output to maven central
 - [QPID-4470](https://issues.apache.org/jira/browse/QPID-4470) - [Java broker] Allow 'maximum queue depth' alerting threshold to be set when declaring queue from JMX/AMQP
 - [QPID-4471](https://issues.apache.org/jira/browse/QPID-4471) - Add docbook for producer transaction timeout feature of Java Broker.
 - [QPID-4502](https://issues.apache.org/jira/browse/QPID-4502) - Document Handing Undeliverable Messages (DLQ/Maximum Delivery Count features)
 - [QPID-4504](https://issues.apache.org/jira/browse/QPID-4504) - Break up Perl classes into separate source modules
 - [QPID-4505](https://issues.apache.org/jira/browse/QPID-4505) - Provide Perl unit tests
 - [QPID-4515](https://issues.apache.org/jira/browse/QPID-4515) - Java Broker: improve logging, especially for diagnosis of transactional messaging performance
 - [QPID-4517](https://issues.apache.org/jira/browse/QPID-4517) - [Java Broker] default log4j configuration outputs line numbers, which is a performance drag
 - [QPID-4533](https://issues.apache.org/jira/browse/QPID-4533) - Java broker performance tests should support writing results to database
 - [QPID-4536](https://issues.apache.org/jira/browse/QPID-4536) - Stop broker automatically using every network interface for fallback addresses
 - [QPID-4538](https://issues.apache.org/jira/browse/QPID-4538) - Event-driven container/library for AMQP - based on Qpid Proton
 - [QPID-4563](https://issues.apache.org/jira/browse/QPID-4563) - Change the Qpid::Messaging::Address constructor to use a URL string
 - [QPID-4568](https://issues.apache.org/jira/browse/QPID-4568) - Improve the Ruby language bindings documentation
 - [QPID-4577](https://issues.apache.org/jira/browse/QPID-4577) - Provide access to enable/disable high resolution timestamps without restarting broker
 - [QPID-4580](https://issues.apache.org/jira/browse/QPID-4580) - Improve the Perl language binding documentation
 - [QPID-4581](https://issues.apache.org/jira/browse/QPID-4581) - Perl message content should be automatically encoded and decoded.
 - [QPID-4586](https://issues.apache.org/jira/browse/QPID-4586) - Allow broker to initiate AMQP 1.0 connections (and links) to other entities
 - [QPID-4587](https://issues.apache.org/jira/browse/QPID-4587) - Improve the quality of the comments in the Perl examples
 - [QPID-4588](https://issues.apache.org/jira/browse/QPID-4588) - Language bindings should load the Swig descriptors from the qpid/qmf directory
 - [QPID-4597](https://issues.apache.org/jira/browse/QPID-4597) - Java broker performance tests should support visualisation of time series data
 - [QPID-4603](https://issues.apache.org/jira/browse/QPID-4603) - Allow qpid-send to set other property types using -P besides strings
 - [QPID-4604](https://issues.apache.org/jira/browse/QPID-4604) - C++ Broker queue creation limits require better granularity 
 - [QPID-4605](https://issues.apache.org/jira/browse/QPID-4605) - Java Performance Test and Visualisation unit tests should subclass QpidTestCase, not TestCase
 - [QPID-4606](https://issues.apache.org/jira/browse/QPID-4606) - Java Performance Test and Visualisation unit test timeouts insufficient for slow CI servers
 - [QPID-4610](https://issues.apache.org/jira/browse/QPID-4610) - Remove code duplication from transport layers of C++ broker
 - [QPID-4615](https://issues.apache.org/jira/browse/QPID-4615) - Give C++ broker on unix ability to import a listening socket opened by parent process
 - [QPID-4632](https://issues.apache.org/jira/browse/QPID-4632) - Change Threshold Alerts from Level-Sensitive to Edge-Triggered
 - [QPID-4636](https://issues.apache.org/jira/browse/QPID-4636) - [Java Broker] add a 'peerstore' to enhance SSL Client Authentication functionality, provide similar 'trusted peer' support with self-signed certs as the C++ broker 
 - [QPID-4638](https://issues.apache.org/jira/browse/QPID-4638) - [Java Broker] Add web UI to create/delete/update authentication providers
 - [QPID-4639](https://issues.apache.org/jira/browse/QPID-4639) - Add UI into web management console to create/delete virtual hosts
 - [QPID-4645](https://issues.apache.org/jira/browse/QPID-4645) - [Java broker] add plugins as runtime dependencies in the broker pom, and make the optional bdbstore module dep scopes in line with other plugins
 - [QPID-4655](https://issues.apache.org/jira/browse/QPID-4655) - [Java Broker] add BrokerOptions support to request the Broker not perform log4j logging configuration when it is being run embedded
 - [QPID-4656](https://issues.apache.org/jira/browse/QPID-4656) - Java Performance Tests - add documentation
 - [QPID-4657](https://issues.apache.org/jira/browse/QPID-4657) - [Java Broker] Add UI into web management console to create/delete/update ports
 - [QPID-4661](https://issues.apache.org/jira/browse/QPID-4661) - [Java Broker] Add UI into web management console to edit broker attributes
 - [QPID-4676](https://issues.apache.org/jira/browse/QPID-4676) - [Java Broker] SSL Client Authentication with username constructed in the same way as on C++ broker
 - [QPID-4699](https://issues.apache.org/jira/browse/QPID-4699) - C++ INSTALL instructions might be clearer if the "Building from a Source Distribution" was moved to the top.
 - [QPID-4725](https://issues.apache.org/jira/browse/QPID-4725) - [Java Broker] HTTP Managament Plugin GUI doesn't show user on connection
 - [QPID-4726](https://issues.apache.org/jira/browse/QPID-4726) - [Java Broker] AMQP 1.0 : Improve SASL support
 - [QPID-4739](https://issues.apache.org/jira/browse/QPID-4739) - [Java Broker] complete functionality to configure multiple key store and trust stores and assign them per-port
 - [QPID-4741](https://issues.apache.org/jira/browse/QPID-4741) - [Java Broker] add command line option to overwrite the broker config store using current initial config
 - [QPID-4742](https://issues.apache.org/jira/browse/QPID-4742) - [Java Broker] add command line option to output a copy of the initial config file
 - [QPID-4746](https://issues.apache.org/jira/browse/QPID-4746) - [Java Broker] add an overriding management-mode authentication provider to restrict access to specific management mode user
 - [QPID-4747](https://issues.apache.org/jira/browse/QPID-4747) - [Java Broker] make specifying the authentication provider mandatory on ports that use them and remove the defaultAuthenticationProvider attribute on the broker
 - [QPID-4752](https://issues.apache.org/jira/browse/QPID-4752) - [Java Broker] complete functionality to configure group providers
 - [QPID-4753](https://issues.apache.org/jira/browse/QPID-4753) - [Java Broker] complete functionality to configure access control providers
 - [QPID-4754](https://issues.apache.org/jira/browse/QPID-4754) - [Java Broker] Make broker name editable and show it in the browser title 
 - [QPID-4755](https://issues.apache.org/jira/browse/QPID-4755) - [Java Broker] Introduce broker attribute for broker supported store types and rename broker attribute 'supportedStoreTypes' into 'supportedVirtualHostStoreTypes'
 - [QPID-4760](https://issues.apache.org/jira/browse/QPID-4760) - Associate Java Broker QueueAdapter and SessionAdapter via ConsumerAdapter
 - [QPID-4761](https://issues.apache.org/jira/browse/QPID-4761) - [Java Broker] Upgrade jetty to 7.6.10.v20130312
 - [QPID-4762](https://issues.apache.org/jira/browse/QPID-4762) - [Java Broker] Upgrade dojo to the version 1.8.3
 - [QPID-4763](https://issues.apache.org/jira/browse/QPID-4763) - [Java Broker] Create generic JDBC store  
 - [QPID-4768](https://issues.apache.org/jira/browse/QPID-4768) - [Java Broker] Resolve compatibility issues in web management console for old versions of IE and FF
 - [QPID-4769](https://issues.apache.org/jira/browse/QPID-4769) - [Java Broker] Add port tab into web management console for consistency with other object tabs
 - [QPID-4773](https://issues.apache.org/jira/browse/QPID-4773) - [Java Broker] Add functionality to display connection errors which might occurs on sending update requests to the broker
 - [QPID-4777](https://issues.apache.org/jira/browse/QPID-4777) - [Java Broker] Add UI to view and edit web management configuration
 - [QPID-4778](https://issues.apache.org/jira/browse/QPID-4778) - [Java Broker] Introduce additional states for configured objects: ERRORED and REPLICA
 - [QPID-4791](https://issues.apache.org/jira/browse/QPID-4791) - [Java Broker] Make it possible to run web management consoles in the same browser from brokers running on the same host but on different ports
 - [QPID-4803](https://issues.apache.org/jira/browse/QPID-4803) - [Java Broker] Ensure the modelVersion and storeVersion attributes are saved to the configuration store and validated at startup
 - [QPID-4809](https://issues.apache.org/jira/browse/QPID-4809) - [Java Broker] add support for specifying configuration properties and use them to default the port numbers and work dir for the initial-config
 - [QPID-4814](https://issues.apache.org/jira/browse/QPID-4814) - [Java Broker] Implement configured objects updates by name and multiple parents
 - [QPID-4815](https://issues.apache.org/jira/browse/QPID-4815) - [Java Broker] make BrokerOptions the primary source for the location of the logging configuration file 
 - [QPID-4817](https://issues.apache.org/jira/browse/QPID-4817) - Add message grouping to Java Broker book
 - [QPID-4824](https://issues.apache.org/jira/browse/QPID-4824) - [Java AMQP 1.0] Reduce memory usage of codec
 - [QPID-4865](https://issues.apache.org/jira/browse/QPID-4865) - HA Update documents for queue replication

## Bugs fixed

 - [QPID-2789](https://issues.apache.org/jira/browse/QPID-2789) - prevent additional message enqueues once a queue has begun to be deleted
 - [QPID-3769](https://issues.apache.org/jira/browse/QPID-3769) - NPE in client AMQDestination.equals()
 - [QPID-4134](https://issues.apache.org/jira/browse/QPID-4134) - Provide Perl language bindings for Qpid
 - [QPID-4240](https://issues.apache.org/jira/browse/QPID-4240) - --link-maintenance-interval option is misspelled
 - [QPID-4274](https://issues.apache.org/jira/browse/QPID-4274) - second invocation of createConsumer fails for queue in JNDI properties
 - [QPID-4281](https://issues.apache.org/jira/browse/QPID-4281) - Java tests logging broken because log4j.configuration is not a valid URL
 - [QPID-4312](https://issues.apache.org/jira/browse/QPID-4312) - [Java client] [0-8/0-9/0-9-1] add option for performing verification of queue existence when sending with a MessageProducer to a Queue destination on a generic Session
 - [QPID-4315](https://issues.apache.org/jira/browse/QPID-4315) - SSL federation doesn't work when used with hostname rather than IP
 - [QPID-4371](https://issues.apache.org/jira/browse/QPID-4371) - The extra_dist/Makefile does not include qpidtypes or stdc++ for building examples
 - [QPID-4388](https://issues.apache.org/jira/browse/QPID-4388) - Systemd support not being installed with Cmake
 - [QPID-4416](https://issues.apache.org/jira/browse/QPID-4416) - perl binding for getContentPtr fails on payloads containing NULL
 - [QPID-4432](https://issues.apache.org/jira/browse/QPID-4432) -  AMQStateManager logger might generate unexpected amount of logs during failover
 - [QPID-4447](https://issues.apache.org/jira/browse/QPID-4447) - C++ Client can hang during connect if heartbeat disconnect fires
 - [QPID-4450](https://issues.apache.org/jira/browse/QPID-4450) - Broker-specific EXTERN includes and macros should not appear in generated QMF code if not used in broker
 - [QPID-4462](https://issues.apache.org/jira/browse/QPID-4462) - [Java Broker] SimpleLDAPAuthenticationManager does not register SASL mechanism PLAIN
 - [QPID-4466](https://issues.apache.org/jira/browse/QPID-4466) - Cannot multiply durations in perl bindings
 - [QPID-4473](https://issues.apache.org/jira/browse/QPID-4473) - [Java Client] Resolve "stream might not be closed" issue reported by findbugs tool in JMSObjectMessage
 - [QPID-4484](https://issues.apache.org/jira/browse/QPID-4484) - C++ qpidmessaging compile error on RHEL 5 gcc 4.1.2
 - [QPID-4485](https://issues.apache.org/jira/browse/QPID-4485) - QMF agent management object list corruption.
 - [QPID-4491](https://issues.apache.org/jira/browse/QPID-4491) - Update JCA Documentation for Property Name Changes
 - [QPID-4492](https://issues.apache.org/jira/browse/QPID-4492) - Provide README Doc for JBoss EAP 6 Configuration
 - [QPID-4493](https://issues.apache.org/jira/browse/QPID-4493) - Memory leak in perl bindings?
 - [QPID-4496](https://issues.apache.org/jira/browse/QPID-4496) - [Java client] Improve error reporting for invalid addresses
 - [QPID-4497](https://issues.apache.org/jira/browse/QPID-4497) - [Java client] Exclusive property for the subscription queue cannot be overridden using the address string
 - [QPID-4507](https://issues.apache.org/jira/browse/QPID-4507) - Perl language bindings not properly mapping uint8_t type
 - [QPID-4513](https://issues.apache.org/jira/browse/QPID-4513) - [Java Client] can erroneously log "Unable to load custom SASL providers." when loaded with multiple class loaders
 - [QPID-4518](https://issues.apache.org/jira/browse/QPID-4518) - Unknown qpidd config-file options should prevent startup.
 - [QPID-4531](https://issues.apache.org/jira/browse/QPID-4531) - Variant.cpp cast of -0 failing with older GCC
 - [QPID-4537](https://issues.apache.org/jira/browse/QPID-4537) - qpid-stat: fix undefined name error
 - [QPID-4540](https://issues.apache.org/jira/browse/QPID-4540) - The subscription queue should only be deleted by the consumer.
 - [QPID-4541](https://issues.apache.org/jira/browse/QPID-4541) - Messages are replayed after XA commit in a failover scenario
 - [QPID-4543](https://issues.apache.org/jira/browse/QPID-4543) - QMF queueMoveMessages method returns "InvalidParameter" exception when there are simply no messages available to move from the source queue - this is confusing.
 - [QPID-4545](https://issues.apache.org/jira/browse/QPID-4545) - AMQP 1.0 support doesn't work under cmake build
 - [QPID-4546](https://issues.apache.org/jira/browse/QPID-4546) - Unable to delete federation routes or links if connection is not up
 - [QPID-4548](https://issues.apache.org/jira/browse/QPID-4548) - Windows packaging doesn't pick up 32-bit ProgramFiles location correctly
 - [QPID-4550](https://issues.apache.org/jira/browse/QPID-4550) - [Java Broker] AMQP 1.0 Persistent Messages cause failure on recovery
 - [QPID-4552](https://issues.apache.org/jira/browse/QPID-4552) - C++ Messaging examples don't build
 - [QPID-4554](https://issues.apache.org/jira/browse/QPID-4554) - QPID tools use of SSL parameter "ssl_keyfile" is incorrect.
 - [QPID-4559](https://issues.apache.org/jira/browse/QPID-4559) - qpid-config deletes queue which contains messages
 - [QPID-4562](https://issues.apache.org/jira/browse/QPID-4562) - Message#reply_to= should auto-wrap the address argument in an Address if the argument is a String
 - [QPID-4564](https://issues.apache.org/jira/browse/QPID-4564) - Decoding method in encoding.rb ignores the return value
 - [QPID-4565](https://issues.apache.org/jira/browse/QPID-4565) - Encoding hashes with embedded hashes converts those to strings.
 - [QPID-4569](https://issues.apache.org/jira/browse/QPID-4569) - AMQP 1.0 module is not loaded in time for examples
 - [QPID-4570](https://issues.apache.org/jira/browse/QPID-4570) - [Java Broker] Multiple AMQP 1.0 Connections cause failure when JMX management enabled
 - [QPID-4576](https://issues.apache.org/jira/browse/QPID-4576) - qpid-receive does not commit ready address message
 - [QPID-4579](https://issues.apache.org/jira/browse/QPID-4579) - Fails to build from source with GCC 4.8.0
 - [QPID-4590](https://issues.apache.org/jira/browse/QPID-4590) - running amqp 1.0 without management causes crash
 - [QPID-4595](https://issues.apache.org/jira/browse/QPID-4595) - Invoking Receiver::fetch() in a loop for slow producer causes only first &lt;prefetch&gt; messages received
 - [QPID-4602](https://issues.apache.org/jira/browse/QPID-4602) - Java broker fails to start if the default log4j configuration is used
 - [QPID-4607](https://issues.apache.org/jira/browse/QPID-4607) - C++ Broker connection limits counting fails and self tests don't catch the errors
 - [QPID-4608](https://issues.apache.org/jira/browse/QPID-4608) - JMS client authorization failure throws JMSException instead of JMSSecurityException
 - [QPID-4609](https://issues.apache.org/jira/browse/QPID-4609) - Incorrect lock in the synchronize statement in org.apache.qpid.server.model.adapter.BrokerAdapter
 - [QPID-4617](https://issues.apache.org/jira/browse/QPID-4617) - getJMSReplyTo does not return null for when ReplyTo property is empty
 - [QPID-4625](https://issues.apache.org/jira/browse/QPID-4625) - Amqp 1.0 message properties (from the application-properties section) cannot be extracted
 - [QPID-4626](https://issues.apache.org/jira/browse/QPID-4626) - Amqp 0-10 Message getProperty() does not correctly return boolean values (or floating point values)
 - [QPID-4629](https://issues.apache.org/jira/browse/QPID-4629) - Improve validation of received amqp 0-10 frames
 - [QPID-4633](https://issues.apache.org/jira/browse/QPID-4633) - C++ broker compile error on RHEL 5 g++ 4.1.2
 - [QPID-4634](https://issues.apache.org/jira/browse/QPID-4634) - C++ broker Boost-related compile errors
 - [QPID-4652](https://issues.apache.org/jira/browse/QPID-4652) - [Java Broker 1.0] Temp queues create for exchange subscriptions not automatically deleted
 - [QPID-4653](https://issues.apache.org/jira/browse/QPID-4653) - [Java Broker 1.0] Implement statistics counting on 1.0 connections
 - [QPID-4654](https://issues.apache.org/jira/browse/QPID-4654) - [Java Client 1.0] Support redirects in Java JMS AMQP 1.0 client
 - [QPID-4658](https://issues.apache.org/jira/browse/QPID-4658) -  XML exchange does not update statistics when no binding key matches routing key
 - [QPID-4666](https://issues.apache.org/jira/browse/QPID-4666) - [Java Broker] Incorrect exception messages returned following 0-10 MessageSubscribe failure
 - [QPID-4667](https://issues.apache.org/jira/browse/QPID-4667) - Selective message acknowledgement does not work over AMQP 1.0
 - [QPID-4669](https://issues.apache.org/jira/browse/QPID-4669) - require proton 0.3 or greater
 - [QPID-4671](https://issues.apache.org/jira/browse/QPID-4671) - [Java Broker] NPE thrown during "exchange.bound" command against a fanout exchange when specifying the name of a queue that does not exist
 - [QPID-4672](https://issues.apache.org/jira/browse/QPID-4672) - C++ Broker deadlock detaching XmlExchange sessions
 - [QPID-4673](https://issues.apache.org/jira/browse/QPID-4673) - [Java Broker AMQP 1.0] Potential for deadlock when draining AMQP 1.0 subscriptions
 - [QPID-4674](https://issues.apache.org/jira/browse/QPID-4674) - [AMQP 1.0] receiver not notified when link is detached by peer
 - [QPID-4675](https://issues.apache.org/jira/browse/QPID-4675) - [AMQP 1.0] handle receiving link from direct exchange even with no filter specified
 - [QPID-4677](https://issues.apache.org/jira/browse/QPID-4677) - [Java Broker] fix incorrect attribute names, group inheritable defaults and add missing ones
 - [QPID-4678](https://issues.apache.org/jira/browse/QPID-4678) - [Java Broker] add ACL to restrict new support for broker-level configuration through the management interface
 - [QPID-4679](https://issues.apache.org/jira/browse/QPID-4679) - [AMQP 1.0] many aspects of address are silently ignored
 - [QPID-4680](https://issues.apache.org/jira/browse/QPID-4680) - [Java Broker] Persistent NoAck messages leave rows in queue entry table even after dequeue (0-9/0-9/0-9-1 codepath)
 - [QPID-4684](https://issues.apache.org/jira/browse/QPID-4684) - Remove obsolete options from example qpidd.conf file.
 - [QPID-4685](https://issues.apache.org/jira/browse/QPID-4685) - [Java Broker] update documentation to reflect changes to configuration etc
 - [QPID-4686](https://issues.apache.org/jira/browse/QPID-4686) - Mention ldconfig in cpp/INSTALL instructions
 - [QPID-4688](https://issues.apache.org/jira/browse/QPID-4688) - [Java Broker] update optional BDB store to use version 5.0.73 of BDB JE
 - [QPID-4692](https://issues.apache.org/jira/browse/QPID-4692) - ACL queue quotas are not updated when auto delete queues are deleted
 - [QPID-4697](https://issues.apache.org/jira/browse/QPID-4697) - Minor fixes to make distcheck
 - [QPID-4698](https://issues.apache.org/jira/browse/QPID-4698) - Fixes needed for the CMake build system when installing files.
 - [QPID-4700](https://issues.apache.org/jira/browse/QPID-4700) - [AMQP 1.0] 'to' field incorrectly mapped on to 'x-amqp-delivery-count' property
 - [QPID-4705](https://issues.apache.org/jira/browse/QPID-4705) - [Java Broker] restrict access to web management interfaces to authenticated and authorised users only
 - [QPID-4714](https://issues.apache.org/jira/browse/QPID-4714) - AMQConnection close can leak socket connections if exceptions occur earlier in the process
 - [QPID-4717](https://issues.apache.org/jira/browse/QPID-4717) - QMF issue on exchange: update timestamp doesn't seem to be getting updated
 - [QPID-4719](https://issues.apache.org/jira/browse/QPID-4719) - Problem building perl bindings from qpid 0.22 RC1 tarball
 - [QPID-4722](https://issues.apache.org/jira/browse/QPID-4722) - qpid-cpp-0.22-rc1 doesnt compile on RHEL6
 - [QPID-4724](https://issues.apache.org/jira/browse/QPID-4724) - qpid-cpp-0.22-rc1 RHEL6 cmake issues
 - [QPID-4729](https://issues.apache.org/jira/browse/QPID-4729) - 0.22 cpp tarball missing a file that breaks cmake
 - [QPID-4731](https://issues.apache.org/jira/browse/QPID-4731) - [Java Broker] unregistering a topic subscription with selector can silently prevent temporary queue deletion
 - [QPID-4751](https://issues.apache.org/jira/browse/QPID-4751) - Hello example still use the 'test' virtualhost, which no longer exists in the initial Java broker config
 - [QPID-4776](https://issues.apache.org/jira/browse/QPID-4776) - Unable to build Ruby language bindings with Cmake 2.6
 - [QPID-4781](https://issues.apache.org/jira/browse/QPID-4781) - cmake build of perl bindings fails in RC2
 - [QPID-4782](https://issues.apache.org/jira/browse/QPID-4782) - [Java Broker] ConnectionAdapter.getSessions() can cause a ConcurrentModificationException
 - [QPID-4784](https://issues.apache.org/jira/browse/QPID-4784) - [Java Broker] simplify PrincipalDatabaseAuthentication manager SASL handling for clarity and to prevent logging erroneous errors when creating additional instances
 - [QPID-4785](https://issues.apache.org/jira/browse/QPID-4785) - [Java Broker] relax restrictions on editing ports outwith management-mode
 - [QPID-4793](https://issues.apache.org/jira/browse/QPID-4793) - qpid/sys/regex.h doesn't detect correct implementation under FreeBSD 9.1
 - [QPID-4795](https://issues.apache.org/jira/browse/QPID-4795) - [Java Broker] update UserManagementMBean name to enable creating multiple credential-managing authentication providers
 - [QPID-4798](https://issues.apache.org/jira/browse/QPID-4798) - use stripped BSD licensed vesions of the amqp spec files
 - [QPID-4799](https://issues.apache.org/jira/browse/QPID-4799) - Move the qpid.pm file to the lib directory.
 - [QPID-4800](https://issues.apache.org/jira/browse/QPID-4800) - Renamed codec.pm to messaging.pm
 - [QPID-4813](https://issues.apache.org/jira/browse/QPID-4813) - [Java Broker] Protect operations to change queue attributes and exchange attributes with ACL
 - [QPID-4818](https://issues.apache.org/jira/browse/QPID-4818) - [Java Broker]  Remove a redundant providerSearchUrl attribute for Simple Ldap Authentication Provider
 - [QPID-4823](https://issues.apache.org/jira/browse/QPID-4823) - [Java Broker] add missing field to web management UI to set the 'alertThresholdQueueDepthBytes' attribute when creating a queue
 - [QPID-4829](https://issues.apache.org/jira/browse/QPID-4829) - [JMS AMQP 1.0] Sessions added to started connections should be automatically started
 - [QPID-4830](https://issues.apache.org/jira/browse/QPID-4830) - [JMS AMQP 1.0] Improve error handling in the JMS client
 - [QPID-4841](https://issues.apache.org/jira/browse/QPID-4841) - [Java Broker] Ensure all data values returned through the REST API are properly sanitised before displaying in HTML to prevent XSS attacks
 - [QPID-4845](https://issues.apache.org/jira/browse/QPID-4845) - [JMS AMQP 1.0] Client incorrectly reports temporary destinations as deleted
 - [QPID-4847](https://issues.apache.org/jira/browse/QPID-4847) - [Java Broker] add support for message group configuration via the HTTP management interface
 - [QPID-4851](https://issues.apache.org/jira/browse/QPID-4851) - [JMS AMQP 1.0] ConcurrentModificationException is thrown on closing of AMQP 1.0 connection with existing sessions
 - [QPID-4852](https://issues.apache.org/jira/browse/QPID-4852) - [Java Broker] Opened AMQP 1.0 connections are not get closed on broker shutdown 
 - [QPID-4855](https://issues.apache.org/jira/browse/QPID-4855) - [AMQP 1.0] compilation error on older compilers
 - [QPID-4856](https://issues.apache.org/jira/browse/QPID-4856) - make distcheck fails on qpid.pm file
 - [QPID-4858](https://issues.apache.org/jira/browse/QPID-4858) - [Java Broker] HTTP management ports configured with 'HTTP' protocol and 'SSL' transport options will silently fail to use SSL
 - [QPID-4860](https://issues.apache.org/jira/browse/QPID-4860) - [Java Broker] Transition virtual host into ERRORED state on failure to activate
 - [QPID-4861](https://issues.apache.org/jira/browse/QPID-4861) - [Java Broker] Allow users to access http management using '/' instead of forcing them to type '/management' or '/index.html'
 - [QPID-4862](https://issues.apache.org/jira/browse/QPID-4862) - [Java Broker] Improve registration/unregistration for JMX MBean objects
 - [QPID-4863](https://issues.apache.org/jira/browse/QPID-4863) - [Java Broker] Validate plugin attribute changes and throw UnsupportedOperationException where attribute changes are not supported
 - [QPID-4868](https://issues.apache.org/jira/browse/QPID-4868) - [Java Broker] Add UI into web management console to edit JMX management configuration
 - [QPID-4869](https://issues.apache.org/jira/browse/QPID-4869) - Small fix: Perl shouldn't be required to build Qpid
 - [QPID-4876](https://issues.apache.org/jira/browse/QPID-4876) - Java Broker should not allow creation of Virtual Host from configuration file having no configuration for the host
 - [QPID-4879](https://issues.apache.org/jira/browse/QPID-4879) - Merged patch removed endif(), breaking CMake build on 0.22
 - [QPID-4881](https://issues.apache.org/jira/browse/QPID-4881) - [Java Broker] new --config-property argument cannot be used with qpid-server.bat (windows)
 - [QPID-4918](https://issues.apache.org/jira/browse/QPID-4918) - Python client does not enforce SSL certificate validation even if CAs configured

## Tasks

 - [QPID-4458](https://issues.apache.org/jira/browse/QPID-4458) - tidy up the gentools directory and move it into the java tree
 - [QPID-4467](https://issues.apache.org/jira/browse/QPID-4467) - base the version number for the maven artefacts on the next release/even version number
 - [QPID-4525](https://issues.apache.org/jira/browse/QPID-4525) - remove ChannelCloseTest and ChannelCloseOkTest system tests
 - [QPID-4526](https://issues.apache.org/jira/browse/QPID-4526) - prevent some extraneous logging during the Java build
 - [QPID-4527](https://issues.apache.org/jira/browse/QPID-4527) - update the JCA module build.xml to use more of the main module.xml targets rather than overriding and reimplementing them itself
 - [QPID-4567](https://issues.apache.org/jira/browse/QPID-4567) - Switch Ruby packaging from Rakefile to gemspec
 - [QPID-4593](https://issues.apache.org/jira/browse/QPID-4593) - [Java Broker] Add a command line option to define file used for initial values
 - [QPID-4594](https://issues.apache.org/jira/browse/QPID-4594) - [Java Broker] Add command line option to start broker in a management mode and options to set JMX and HTTP ports in management mode
 - [QPID-4596](https://issues.apache.org/jira/browse/QPID-4596) - [Java Broker] Add ability to create/delete/update virtual host, authentication provider, port via REST interfaces
