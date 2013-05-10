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

# Qpid Proton 0.4 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid
Proton](file:///home/jross/transom/output/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-184](https://issues.apache.org/jira/browse/PROTON-184) - [Proton-J] Separate API from Pure Java Implementation
 - [PROTON-191](https://issues.apache.org/jira/browse/PROTON-191) - Proton-API reconciliation reporting tool
 - [PROTON-192](https://issues.apache.org/jira/browse/PROTON-192) - Implement Proton-JNI binding for proton-c
 - [PROTON-194](https://issues.apache.org/jira/browse/PROTON-194) - Change proton's build systems to allow for the creation of a Java binding for proton-c.
 - [PROTON-195](https://issues.apache.org/jira/browse/PROTON-195) - Move JythonTests and proton_tests/*.py into system-test module
 - [PROTON-197](https://issues.apache.org/jira/browse/PROTON-197) - Add "small buffer" test to SSL tests
 - [PROTON-199](https://issues.apache.org/jira/browse/PROTON-199) - [Proton-c] Python binding requires python 2.6+
 - [PROTON-208](https://issues.apache.org/jira/browse/PROTON-208) - Create an upstream Perl language tarball
 - [PROTON-210](https://issues.apache.org/jira/browse/PROTON-210) - Proton release.sh should create a single release tarball for proton-c/proton-j
 - [PROTON-217](https://issues.apache.org/jira/browse/PROTON-217) - cmake build system should include "install" target for Java binaries
 - [PROTON-218](https://issues.apache.org/jira/browse/PROTON-218) - Remove dependency on Maven 3
 - [PROTON-224](https://issues.apache.org/jira/browse/PROTON-224) - Python test framework: automatically treat ProtonUnsupportedOperationException as a skipped test
 - [PROTON-242](https://issues.apache.org/jira/browse/PROTON-242) - Shared library used JNI code has poor name "libproton-swig.so"
 - [PROTON-66](https://issues.apache.org/jira/browse/PROTON-66) - Driver implementation for proton-j

## Bugs fixed

 - [PROTON-100](https://issues.apache.org/jira/browse/PROTON-100) - Clean up examples README.txt file
 - [PROTON-166](https://issues.apache.org/jira/browse/PROTON-166) - message.h: pn_message() should be declared pn_message(void)
 - [PROTON-183](https://issues.apache.org/jira/browse/PROTON-183) - intermittent hanging in messenger tests
 - [PROTON-203](https://issues.apache.org/jira/browse/PROTON-203) - pn_listener_set_context() not wrapped correctly in the python bindings
 - [PROTON-204](https://issues.apache.org/jira/browse/PROTON-204) - Handling of partial messages is broken in java messenger
 - [PROTON-205](https://issues.apache.org/jira/browse/PROTON-205) - java messenger does not set source  and target correctly
 - [PROTON-219](https://issues.apache.org/jira/browse/PROTON-219) - Move Cmake modules to the tools directory
 - [PROTON-222](https://issues.apache.org/jira/browse/PROTON-222) - pn_messenger_send returns before message data has been written to the wire
 - [PROTON-230](https://issues.apache.org/jira/browse/PROTON-230) - pn_data_appendn is not exiting the node tree correctly
 - [PROTON-235](https://issues.apache.org/jira/browse/PROTON-235) - SASL layer can "replicate" inbound SASL frames under some circumstances.
 - [PROTON-243](https://issues.apache.org/jira/browse/PROTON-243) - 0.4 RC1 libqpid-proton not found 
 - [PROTON-245](https://issues.apache.org/jira/browse/PROTON-245) - Use of "inline" function specifier not compatible with older versions of swig
 - [PROTON-292](https://issues.apache.org/jira/browse/PROTON-292) - [proton-hawtdispatch] avoid printing debug info to the console.
 - [PROTON-293](https://issues.apache.org/jira/browse/PROTON-293) - [proton-hawtdispatch] Use more conservative initial message size estimates.

## Tasks

 - [PROTON-196](https://issues.apache.org/jira/browse/PROTON-196) - Automate the running of system tests on Apache CI