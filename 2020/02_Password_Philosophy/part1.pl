#!/usr/bin/env perl6

my $input = "input".IO.slurp;
open FH, "input" or die;
my $counter = 0;

for (<FH>) {
    chomp;
    my ($policy, $pass)= split ": ", $_;
    my ($a,$b,$letter) = $policy =~ m/^(\d+)-(\d+) (\w)/;
    my $c = () = $pass =~ /$letter/g;
    if ($a <= $c and $c <= $b) { $counter++ };
}

print $counter;

