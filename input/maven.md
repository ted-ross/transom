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

# Qpid via Maven

Qpid JMS is available via the [Maven central
repository](http://maven.apache.org/guides/mini/guide-central-repository-upload.html). The
following dependencies can be added to the POM for your Maven build.

## Qpid JMS

    <dependency>
      <groupId>org.apache.qpid</groupId>
      <artifactId>qpid-client</artifactId>
      <version>@current-release@</version>
    </dependency>



## Qpid AMQP 1.0 JMS

    <dependency>
      <groupId>org.apache.qpid</groupId>
      <artifactId>qpid-amqp-1-0-client-jms</artifactId>
      <version>@current-release@</version>
    </dependency>

## JMS interface definition

You will need the JMS interface definition if it is not already
available in your environment.  An example dependency for this would
be the following.

    <dependency>
      <groupId>org.apache.geronimo.specs</groupId>
      <artifactId>geronimo-jms_1.1_spec</artifactId>
      <version>1.0</version>
    </dependency>

## More information

 - [Maven project](http://maven.apache.org/)
 - [Maven central repository](http://maven.apache.org/guides/mini/guide-central-repository-upload.html)
