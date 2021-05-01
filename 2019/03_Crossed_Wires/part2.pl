#!/usr/bin/perl

$x = $y = 100000;
$xstart = $ystart = $x;
%t;
$rl = 1;
$gl = 1;

sub move(@) {
    $dir = shift;
    $col = shift;
    $m = shift;
    $mov = 1;
    while ($mov <= $m) {
        do { $xx = $x+$mov; $yy = $y} if $dir eq 'r';
        do { $xx = $x-$mov; $yy = $y} if $dir eq 'l';
        do { $xx = $x; $yy = $y-$mov} if $dir eq 'u';
        do { $xx = $x; $yy = $y+$mov} if $dir eq 'd';

        if ($col eq 'green' and defined $t{'red'}{$xx}{$yy}) {
            $t{$col}{$xx}{$yy} = $gl++;
            print(($t{'red'}{$xx}{$yy} + $t{'green'}{$xx}{$yy}) . "\t t=$xx,$yy\n");
        } else {
            $t{$col}{$xx}{$yy} = $rl++ if $col eq 'red';
            $t{$col}{$xx}{$yy} = $gl++ if $col eq 'green';
        }
        $mov++;
    }
    $x += $m if $dir eq 'r';
    $x -= $m if $dir eq 'l';
    $y -= $m if $dir eq 'u';
    $y += $m if $dir eq 'd';

}

open FH, "<input2" or die;
$_ = <FH>; chomp;
@red = split ',', $_;
$_ = <FH>; chomp;
@green = split ',', $_;
close FH;


for (@red) {
    if (/R/) {
        s/^\w//;
        move(r,red,$_);
    }
    elsif (/L/) {
        s/^\w//;
        move(l,red,$_);
    }
    elsif (/U/) {
        s/^\w//;
        move(u,red,$_);
    }
    elsif (/D/) {
        s/^\w//;
        move(d,red,$_);
    }
}

$x = $y = $xstart;

for (@green) {
    if (/R/) {
        s/^\w//;
        move(r,green,$_);
    }
    elsif (/L/) {
        s/^\w//;
        move(l,green,$_);
    }
    elsif (/U/) {
        s/^\w//;
        move(u,green,$_);
    }
    elsif (/D/) {
        s/^\w//;
        move(d,green,$_);
    }
}

