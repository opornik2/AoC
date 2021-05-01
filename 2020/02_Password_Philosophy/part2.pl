#!/usr/bin/env perl

open FH, "input" or die;
my $counter = 0;

for (<FH>) {
    chomp;
    my ($policy, $pass)= split ": ", $_;
    my ($a,$b,$letter) = $policy =~ m/^(\d+)-(\d+) (\w)/;
    @p = split //, $pass;
    if ( ($p[$a-1] eq $letter and $p[$b-1] ne $letter) or
         ($p[$a-1] ne $letter and $p[$b-1] eq $letter) ) {
         $counter++;
    }
}

print $counter;

