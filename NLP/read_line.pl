#!/usr/bin/perl
use strict;
use warnings;

print "What is your name, son? ";
my $name = <>; # Read from stdin.
chomp $name; # Removes trailing newline.
print "Hello, my friend $name!\n";
