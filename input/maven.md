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

;; Fragments generated with 'pygmentize -l xml -f html ~/maven.xml > ~/maven.html'

## Qpid JMS

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.qpid<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>qpid-client<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>@current-release@<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>

## Qpid AMQP 1.0 JMS

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.qpid<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>qpid-amqp-1-0-client-jms<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>@current-release@<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>

## JMS interface definition

You will need the JMS interface definition if it is not already
available in your environment.  An example dependency for this would
be the following.

<div class="highlight"><pre>
<span class="nt">&lt;dependency&gt;</span>
  <span class="nt">&lt;groupId&gt;</span>org.apache.geronimo.specs<span class="nt">&lt;/groupId&gt;</span>
  <span class="nt">&lt;artifactId&gt;</span>geronimo-jms_1.1_spec<span class="nt">&lt;/artifactId&gt;</span>
  <span class="nt">&lt;version&gt;</span>1.0<span class="nt">&lt;/version&gt;</span>
<span class="nt">&lt;/dependency&gt;</span>
</pre></div>

## More information

 - [Snapshot repository](https://repository.apache.org/content/repositories/snapshots/)
 - [Maven project](http://maven.apache.org/)
 - [Maven central repository](http://maven.apache.org/guides/mini/guide-central-repository-upload.html)
