my ($wc,$sc) = (0,0);
while (<>) {
    while (/\w+|[.!?]+/) {
	my $word = $&; $_ = $';
        if ($word =~ /^[.!?]+$/) { ++$sc; }
        else { ++$wc; }
    }
}
print "Words: $wc\nSentences: $sc\n";
