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

Qpid employs
[revision control](http://en.wikipedia.org/wiki/Revision_control) to
track and manage changes to its source code.  Qpid uses the
[Subversion](http://subversion.apache.org/) revision control system.

## Browse the code

 - [Browse via ViewVC](http://svn.apache.org/viewvc/qpid/trunk/qpid)
 - [Browse the source tree directly](https://svn.apache.org/repos/asf/qpid/trunk/qpid)
 - <form id="viewvc-goto-form" action="http://svn.apache.org/viewvc" method="get"><input type="hidden" name="view" value="revision"/>Go to revision <input type="text" name="revision"/></form>

## Check out the code

To access the repository anonymously, use the `svn checkout` command
with the following URL:

    % svn checkout http://svn.apache.org/repos/asf/qpid/trunk/qpid

To access the repository as a committer (note the use of *`https`*):

    % svn checkout https://svn.apache.org/repos/asf/qpid/trunk/qpid

When adding files to Subversion, it's important that the appropriate
Subversion properties are set. The client can do it automatically by
modifying the `auto-props` section of the Subversion config file.  Use
the contents of
<http://svn.apache.org/repos/asf/qpid/trunk/qpid/etc/svn-auto-props>.

## Install the code

Consult the install documentation below.

 - [How to build Qpid Java](https://cwiki.apache.org/qpid/qpid-java-build-how-to.html)
 - [Installing and Using Qpid Java](https://cwiki.apache.org/qpid/getting-started-guide.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/trunk/qpid/cpp/INSTALL)
 - [Installing Qpid Proton](http://svn.apache.org/repos/asf/qpid/proton/trunk/README)
 - [Installing Qpid Python](http://svn.apache.org/repos/asf/qpid/trunk/qpid/python/README.txt)
 - [Installing Qpid WCF](http://svn.apache.org/repos/asf/qpid/trunk/qpid/wcf/ReadMe.txt)

## Git

A read-only [Git](http://git-scm.com/) mirror is available.  Use one
of the following commands.

    % git clone git://git.apache.org/qpid.git qpid

    % git clone http://git.apache.org/qpid.git qpid

If you have commit access, it's also possible to commit back with `git
svn dcommit` by following the instructions on the
[Git at Apache](http://www.apache.org/dev/git.html) page.

## More information

 - [Subscribe to commit notifications](@site-url@/resources.html#notifications)
 - [Subversion project](http://subversion.apache.org/)
 - [Subversion manual](http://svnbook.red-bean.com/)
 - [Subversion at Apache](http://www.apache.org/dev/version-control.html)
 - [Git project](http://git-scm.com)
 - [Git documentation](http://git-scm.com/documentation)
 - [Git at Apache](http://www.apache.org/dev/git.html)
