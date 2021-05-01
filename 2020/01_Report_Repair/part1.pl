#!/usr/bin/env perl6

my $input = "input".IO.slurp;
my @input = split "\n", $input;

for (@input.combinations: 2) {
    if ($_[0] + $_[1] == 2020) {
        my $a = $_[0] * $_[1];
        say $_[0];
        say $_[1];
        say $a;
    }
}

