#! /usr/bin/perl5
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
use strict;
use warnings;
use Data::Dumper;

use cqpid_perl;

my $url               = ( @ARGV > 0 ) ? $ARGV[0] : "amqp:tcp:127.0.0.1:5672";
my $address           = ( @ARGV > 1 ) ? $ARGV[1] : "message_queue; {create: always}";
my $connectionOptions = ( @ARGV > 2 ) ? $ARGV[2] : "";

my $connection = new cqpid_perl::Connection($url, $connectionOptions);

eval {
    $connection->open();

    my $session = $connection->createSession();
    my $sender  = $session->createSender($address);

    my $message = new cqpid_perl::Message();
    my $content = { id   => 987654321, 
                    name => "Widget", 
                    percent => sprintf("%.2f", 0.99), 
                    colours => [ qw (red green white) ], 
                   };
    cqpid_perl::encode($content, $message);
    $sender->send($message, 1);

    $connection->close();
};

die $@ if ($@);
