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

# Releases

In addition to the source releases below, there are more [ways to get
Qpid](@site-url@/get-qpid.html).

## Current releases

 - @current-release-link@
 - @current-proton-release-link@

## Past releases

 - [Qpid 0.18](qpid-0.18/index.html)
 - [Qpid 0.16](qpid-0.16/index.html)
 - [Qpid 0.14](qpid-0.14/index.html)

Still older releases are available at
<http://archive.apache.org/dist/qpid/>.

## Verify what you download

It is essential that you verify the integrity of the downloaded files
using the PGP signatures or SHA1 checksums.

The PGP signatures can be verified using PGP or GPG. First download
the [KEYS](http://www.apache.org/dist/qpid/KEYS) file as well as the
<code>.asc</code> PGP signature file for the relevant artefact. Make
sure you get these files from the relevant subdirectory of the [main
distribution directory](http://www.apache.org/dist/qpid/), rather than
from a mirror. Then verify the signatures using one of the following
sets of commands.

    % pgpk -a KEYS
    % pgpv qpid-0.@current-release@.tar.gz.asc

    % pgp -ka KEYS
    % pgp qpid-@current-release@.tar.gz.asc

    % gpg --import KEYS
    % gpg --verify qpid-@current-release@.tar.gz.asc

Alternatively, you can verify the SHA1 checksum of the files. A unix
program called sha1 or sha1sum is included in many unix
distributions. It is also available as part of [GNU
Textutils](http://www.gnu.org/software/textutils/textutils.html). For
Windows users, [fsum](http://www.slavasoft.com/fsum/) supports
SHA1. Ensure your generated checksum string matches the string
published in the SHA1SUM file included with each release. Again, make
sure you get this file from the relevant subdirectory of the [main
distribution directory](http://www.apache.org/dist/qpid/), rather than
from a mirror.

## Release process

Qpid produces three releases a year on a time-based schedule.  They
usually drop in January, April, and August.  New releases are
announced on the [Qpid mailing lists](@site-url@/mailing-lists.html)
and the
[Apache announce list](http://mail-archives.apache.org/mod_mbox/www-announce/).
