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

# Source Code

Qpid uses [Subversion](http://subversion.apache.org/) to manage its
source code.

## Browse the code

You can see all of Qpid's source code via the [repository web
interface](http://svn.apache.org/viewvc/qpid/trunk/qpid).

## Check out the code

### Subversion

To access the repository anonymously, use
[Subversion](http://subversion.apache.org/) to check out
<http://svn.apache.org/repos/asf/qpid/trunk/qpid>.

    % svn co http://svn.apache.org/repos/asf/qpid/trunk/qpid

To access the repository as a committer, use <https://svn.apache.org/repos/asf/qpid/trunk/qpid>.

    % svn co https://svn.apache.org/repos/asf/qpid/trunk/qpid

When adding files to subversion, it's important that the appropriate
Subversion properties are set. The client can do it automatically by
modifying the <code>auto-props</code> section of the Subversion config
file.  Use the contents of <http://svn.apache.org/repos/asf/qpid/trunk/qpid/etc/svn-auto-props>.

### Git

A read-only [Git](http://git-scm.com/) mirror is available.  Use one
of the following commands.

    % git clone git://git.apache.org/qpid.git qpid

    % git clone http://git.apache.org/qpid.git qpid

If you have commit access, it's also possible to commit back with
<code>git svn dcommit</code> by following the instructions on the [Git
at Apache](http://www.apache.org/dev/git.html) page.

## Install the code

Consult the install documentation below.

 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/trunk/qpid/cpp/INSTALL)
 - [Installing Qpid Proton](http://svn.apache.org/repos/asf/qpid/proton/trunk/README)
 - [Installing Qpid WCF](http://svn.apache.org/repos/asf/qpid/trunk/qpid/wcf/ReadMe.txt)
 - [How to build Qpid Java](https://cwiki.apache.org/qpid/qpid-java-build-how-to.html)
 - [Installing and Using Qpid Java](https://cwiki.apache.org/qpid/getting-started-guide.html)

## More information

 - [Repository web interface](http://svn.apache.org/viewvc/qpid/trunk/qpid)
 - [Subversion project](http://subversion.apache.org/)
 - [Subversion manual](http://svnbook.red-bean.com/)
 - [Subversion at Apache](http://www.apache.org/dev/version-control.html)
 - [Git project](http://git-scm.com)
 - [Git documentation](http://git-scm.com/documentation)
 - [Git at Apache](http://www.apache.org/dev/git.html)
