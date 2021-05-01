#!/usr/bin/env perl6

my $input = "input".IO.slurp;
my @input = split "\n", $input;

for (@input.combinations: 3) {
    if ($_[0] + $_[1] + $_[2] == 2020) {
        my $a = $_[0] * $_[1] * $_[2];
        say $_[0];
        say $_[1];
        say $_[2];
        say $a;
        exit;
    }
}

