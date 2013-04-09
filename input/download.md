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

# Download

*In addition to the source artefacts below, there are
[more ways to get Qpid](@site-url@/get-qpid.html).*

It's important to [verify the integrity](#verify-what-you-download) of
the files you download.

## Messaging APIs

  || *Content* || *Download* || *Signature* ||
  || [AMQP Messenger](@site-url@/components/messenger/index.html), [AMQP Protocol Engine](@site-url@/components/protocol-engine/index.html) (C, bindings) || [qpid-proton-c-@current-proton-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/proton/@current-proton-release@/qpid-proton-c-@current-proton-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/proton/@current-proton-release@/qpid-proton-c-@current-proton-release@.tar.gz.asc) ||
  || [AMQP Messenger](@site-url@/components/messenger/index.html), [AMQP Protocol Engine](@site-url@/components/protocol-engine/index.html) (Java) || [qpid-proton-j-@current-proton-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/proton/@current-proton-release@/qpid-proton-j-@current-proton-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/proton/@current-proton-release@/qpid-proton-j-@current-proton-release@.tar.gz.asc) ||
  || [Qpid JMS](@site-url@/components/qpid-jms/index.html)\* (AMQP 0-10, 0-91, 0-9, 0-8) || [qpid-java-client-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-java-client-@current-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-java-client-@current-release@.tar.gz.asc) ||
  || [Qpid JMS](@site-url@/components/qpid-jms/index.html)\* (AMQP 1.0) || [qpid-java-amqp-1-0....tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-java-amqp-1-0-client-@current-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-java-amqp-1-0-client-@current-release@.tar.gz.asc) ||
  || [Qpid Messaging API](@site-url@/components/messaging-api/index.html) (C++, bindings) || [qpid-cpp-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-cpp-@current-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-cpp-@current-release@.tar.gz.asc) ||
  || [Qpid Messaging API](@site-url@/components/messaging-api/index.html) (Python) || [qpid-python-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-python-@current-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-python-@current-release@.tar.gz.asc) ||
  || [Qpid WCF](@site-url@/components/qpid-wcf/index.html) || [qpid-wcf-@current-release@.zip](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-wcf-@current-release@.zip) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-wcf-@current-release@.zip.asc) ||

## Servers and tools

  || *Content* || *Download* || *Signature* ||
  || [Java broker](@site-url@/components/java-broker/index.html)\* || [qpid-java-broker-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-java-broker-@current-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-java-broker-@current-release@.tar.gz.asc) ||
  || [C++ broker](@site-url@/components/cpp-broker/index.html) || [qpid-cpp-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-cpp-@current-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-cpp-@current-release@.tar.gz.asc) ||
  || C++ broker command-line tools || [qpid-tools-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-tools-@current-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-tools-@current-release@.tar.gz.asc) ||
  || [Qpid JCA](@site-url@/components/qpid-jca/index.html)\* || [qpid-java-broker-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-java-@current-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-java-@current-release@.tar.gz.asc) ||
  || [QMF](@site-url@/components/qmf/index.html) || [qpid-qmf-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-qmf-@current-release@.tar.gz) || [PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-qmf-@current-release@.tar.gz.asc) ||

\*These Java artefacts are released as compiled bytecode.  We also
offer the source as part of our
[full source release](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-@current-release@.tar.gz)
([PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-@current-release@.tar.gz.asc)).

## Verify what you download

It is essential that you verify the integrity of the downloaded files
using the PGP signatures or SHA1 checksums.

The PGP signatures can be verified using PGP or GPG. First download
the [`KEYS`](http://www.apache.org/dist/qpid/KEYS) file as well as the
`.asc` PGP signature file for the relevant artefact. Make sure you get
these files from the relevant subdirectory of the
[main distribution directory](http://www.apache.org/dist/qpid/),
rather than from a mirror. Then verify the signatures using one of the
following sets of commands.

    % pgpk -a KEYS
    % pgpv qpid-0.@current-release@.tar.gz.asc

    % pgp -ka KEYS
    % pgp qpid-@current-release@.tar.gz.asc

    % gpg --import KEYS
    % gpg --verify qpid-@current-release@.tar.gz.asc

Alternatively, you can verify the SHA1 checksum of the files. A unix
program called `sha1` or `sha1sum` is included in many unix
distributions. It is also available as part of
[GNU Textutils](http://www.gnu.org/software/textutils/textutils.html). For
Windows users, [FSUM](http://www.slavasoft.com/fsum/) supports
SHA1. Ensure your generated checksum string matches the string
published in the `SHA1SUM` file included with each release. Again,
make sure you get this file from the relevant subdirectory of the
[main distribution directory](http://www.apache.org/dist/qpid/),
rather than from a mirror.

## Qpid releases

Qpid's source artefacts are produced as part of our community release
process.  The downloads on this page are from our current releases,
@current-release-link@ and @current-proton-release-link@.

 - [Find past releases](@site-url@/releases/index.html#past-releases) 
 - More about [Qpid releases](@site-url@/releases/index.html)
