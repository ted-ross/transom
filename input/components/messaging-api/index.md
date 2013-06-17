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

# Qpid Messaging API

A connection-oriented messaging API that supports many languages and
platforms.

  || *Languages* || C++, Perl, Python, Ruby, .NET ||
  || *Platforms* || Linux, Windows ||
  || *AMQP versions* || 1.0, 0-10 ||
  || *Downloads* || C++, bindings: [qpid-cpp-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-cpp-@current-release@.tar.gz) \[[PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-cpp-@current-release@.tar.gz.asc)],<br/>Python: [qpid-python-@current-release@.tar.gz](http://www.apache.org/dyn/closer.cgi/qpid/@current-release@/qpid-python-@current-release@.tar.gz) \[[PGP](http://www.apache.org/dist/qpid/@current-release@/qpid-python-@current-release@.tar.gz.asc)] ||
  || *Source locations* ||  <http://svn.apache.org/repos/asf/qpid/trunk/qpid/cpp/>,<br/> <http://svn.apache.org/repos/asf/qpid/trunk/qpid/python/> ||
  || *Issues* || [Open bugs](https://issues.apache.org/jira/issues/?jql=project%20%3D%20QPID%20AND%20issuetype%20%3D%20Bug%20AND%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20AND%20status%20in%20\(Open%2C%20Reopened%2C%20%22In%20Progress%22%2C%20%22Ready%20To%20Review%22\)), [Completed enhancements](https://issues.apache.org/jira/issues/?jql=project%20%3D%20QPID%20AND%20issuetype%20in%20\(%22New%20Feature%22%2C%20Improvement\)%20AND%20resolution%20%3D%20Fixed%20AND%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20AND%20status%20in%20\(Closed%2C%20Resolved\)), [Requested enhancements](https://issues.apache.org/jira/issues/?jql=project%20%3D%20QPID%20AND%20issuetype%20in%20\(%22New%20Feature%22%2C%20Improvement\)%20AND%20component%20in%20\(%22C%2B%2B%20Client%22%2C%20%22Dot%20Net%20Client%22%2C%20%22Perl%20Client%22%2C%20%22Python%20Client%22%2C%20%22Ruby%20Client%22\)%20AND%20status%20in%20\(Open%2C%20Reopened%2C%20%22In%20Progress%22%2C%20%22Ready%20To%20Review%22\)) ||

## Documentation

This is the documentation for the current released version.  You can
find previous versions with our
[past releases](@site-url@/releases/index.html#past-releases).

 - [Using the Qpid Messaging API](@current-release-url@/programming/book/ch02.html)

<div class="two-column" markdown="1">
<div class="column" markdown="1">

### C++

 - [API reference](@current-release-url@/messaging-api/cpp/api/index.html)
 - [Examples](@current-release-url@/messaging-api/cpp/examples/index.html)
 - [Installing Qpid C++](http://svn.apache.org/repos/asf/qpid/tags/@current-release@/qpid/cpp/INSTALL)

### Perl

 - [Examples](@current-release-url@/messaging-api/perl/examples/index.html)

### Python

 - [API reference](@current-release-url@/messaging-api/python/api/index.html)
 - [Examples](@current-release-url@/messaging-api/python/examples/index.html)
 - [Installing Qpid Python](http://svn.apache.org/repos/asf/qpid/tags/@current-release@/qpid/python/README.txt)

</div>
<div class="column" markdown="1">

### Ruby

 - [API reference](@current-release-url@/messaging-api/ruby/api/index.html)
 - [Examples](@current-release-url@/messaging-api/ruby/examples/index.html)
 - [Installing the Ruby Messaging API](http://svn.apache.org/repos/asf/qpid/tags/@current-release@/qpid/cpp/bindings/qpid/ruby/README.rdoc)

### .NET

 - [The .NET Binding for the C++ Messaging Client](@current-release-url@/programming/book/ch05.html)
 - [API reference](@current-release-url@/messaging-api/dotnet/api/index.html)
 - [Examples](@current-release-url@/messaging-api/dotnet/examples/index.html)
 - [Installing the .NET Messaging API](http://svn.apache.org/repos/asf/qpid/tags/@current-release@/qpid/cpp/bindings/qpid/dotnet/ReadMe.txt)

</div>
</div>

### Examples

  || *C++* || [hello_world.cpp](@current-release-url@/messaging-api/cpp/examples/hello_world.cpp.html) || [client.cpp](@current-release-url@/messaging-api/cpp/examples/client.cpp.html) || [server.cpp](@current-release-url@/messaging-api/cpp/examples/server.cpp.html) || [spout.cpp](@current-release-url@/messaging-api/cpp/examples/spout.cpp.html) || [drain.cpp](@current-release-url@/messaging-api/cpp/examples/drain.cpp.html) ||
  || *Perl* || [hello_world.pl](@current-release-url@/messaging-api/perl/examples/hello_world.pl.html) || [client.pl](@current-release-url@/messaging-api/perl/examples/client.pl.html) || [server.pl](@current-release-url@/messaging-api/perl/examples/server.pl.html) || [spout.pl](@current-release-url@/messaging-api/perl/examples/spout.pl.html) || [drain.pl](@current-release-url@/messaging-api/perl/examples/drain.pl.html) ||
  || *Python* || [hello](@current-release-url@/messaging-api/python/examples/hello.html) ||  ||  || [spout](@current-release-url@/messaging-api/python/examples/spout.html) || [drain](@current-release-url@/messaging-api/python/examples/drain.html) ||
  || *Ruby* || [hello_world.rb](@current-release-url@/messaging-api/ruby/examples/hello_world.rb.html) || [client.rb](@current-release-url@/messaging-api/ruby/examples/client.rb.html) || [server.rb](@current-release-url@/messaging-api/ruby/examples/server.rb.html) || [spout.rb](@current-release-url@/messaging-api/ruby/examples/spout.rb.html) || [drain.rb](@current-release-url@/messaging-api/ruby/examples/drain.rb.html) ||
  || *.NET* || [helloworld.cs](@current-release-url@/messaging-api/dotnet/examples/csharp.example.helloworld.cs.html) || [client.cs](@current-release-url@/messaging-api/dotnet/examples/csharp.example.client.cs.html) || [server.cs](@current-release-url@/messaging-api/dotnet/examples/csharp.example.server.cs.html) || [spout.cs](@current-release-url@/messaging-api/dotnet/examples/csharp.example.spout.cs.html) || [drain.cs](@current-release-url@/messaging-api/dotnet/examples/csharp.example.drain.cs.html) ||
