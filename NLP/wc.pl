#!/usr/bin/perl

my $wc = 0;
while (<>) {
    while (/\w+/g) { ++$wc; }
}
print "$wc\n";
