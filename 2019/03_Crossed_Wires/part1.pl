#!/usr/bin/perl

my $x = $y = 1000;
my $xstart = $ystart = $x;
my %t;

sub r(@) {
    $col = shift;
    $m = shift;
    $mov = 1;
    while ($mov <= $m) {
        if ($t{$x+$mov}{$y} eq 'red' and $col eq 'green') {
            $t{$x+$mov}{$y} = 'cross';
            print(abs($x+$mov-$xstart)+abs($y-$ystart),"\t");
            print("t=" . ($x+$mov) . "," . $y . "\n");

        } else {
            $t{$x+$mov}{$y} = $col;
        }
        $mov++;
    }
    $x += $m;
}
sub l(@) {
    $col = shift;
    $m = shift;
    $mov = 1;
    while ($mov <= $m) {
        if ($t{$x-$mov}{$y} eq 'red' and $col eq 'green') {
            $t{$x-$mov}{$y} = 'cross';
            print(abs($x-$mov-$xstart)+abs($y-$ystart),"\t");
            print("t=" . ($x-$mov) . "," . $y . "\n");
        } else {
            $t{$x-$mov}{$y} = $col;
        }
        $mov++;
    }
    $x -= $m;
}
sub u(@) {
    $col = shift;
    $m = shift;
    $mov = 1;
    while ($mov <= $m) {
        if ($t{$x}{$y-$mov} eq 'red' and $col eq 'green') {
            $t{$x}{$y-$mov} = 'cross';
            print(abs($x-$xstart)+abs($y-$mov-$ystart),"\t");
            print("t=" . $x . "," . ($y-$mov) . "\n");
        } else {
            $t{$x}{$y-$mov} = $col;
        }
        $mov++;
    }
    $y -= $m;
}
sub d(@) {
    $col = shift;
    $m = shift;
    $mov = 1;
    while ($mov <= $m) {
        if ($t{$x}{$y+$mov} eq 'red' and $col eq 'green') {
            $t{$x}{$y+$mov} = 'cross';
            print(abs($x-$xstart)+abs($y+$mov-$ystart),"\t");
            print("t=" . $x . "," . ($y+$mov) . "\n");
        } else {
            $t{$x}{$y+$mov} = $col;
        }
        $mov++;
    }
    $y += $m;
}


open FH, "<input" or die;
$_ = <FH>; chomp;
@red = split ',', $_;
$_ = <FH>; chomp;
@green = split ',', $_;
close FH;


for (@red) {
    if (/R/) {
        s/^\w//;
        r(red,$_);
    }
    elsif (/L/) {
        s/^\w//;
        l(red,$_);
    }
    elsif (/U/) {
        s/^\w//;
        u(red,$_);
    }
    elsif (/D/) {
        s/^\w//;
        d(red,$_);
    }
}

$x = $y = $xstart;

for (@green) {
    if (/R/) {
        s/^\w//;
        r(green,$_);
    }
    elsif (/L/) {
        s/^\w//;
        l(green,$_);
    }
    elsif (/U/) {
        s/^\w//;
        u(green,$_);
    }
    elsif (/D/) {
        s/^\w//;
        d(green,$_);
    }
}

