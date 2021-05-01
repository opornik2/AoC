#!/usr/bin/perl

$max = 265149;
$part = 2;
$x = 1000;
$y = 1000;
$val = 1;
$t[$x][$y] = $val;
$last = "d";

sub r() {
    $x += 1;
    $last = "r";
}
sub l() {
    $x -= 1;
    $last = "l";
}
sub u() {
    $y -= 1;
    $last = "u";
}
sub d() {
    $y += 1;
    $last = "d";
}


do {
   if ($last eq "r") {
        if (not defined $t[$x][$y-1]) { u(); }
        else { r(); }
    }
    elsif ($last eq "u") {
        if (not defined $t[$x-1][$y]) { l(); }
        else { u(); }
    }
    elsif ($last eq "l") {
        if (not defined $t[$x][$y+1]) { d(); }
        else { l(); }
    }
    elsif ($last eq "d") {
        if (not defined $t[$x+1][$y]) { r(); }
        else { d(); }
    }
    if ($part == 1) {
        $val += 1 if $part == 1;
    } else {
        $val =  $t[$x-1][$y-1] + $t[$x][$y-1] + $t[$x+1][$y-1] +
            $t[$x-1][$y] + $t[$x+1][$y] +
            $t[$x-1][$y+1] + $t[$x][$y+1] + $t[$x+1][$y+1];
    }
    $t[$x][$y] = $val;
    print($x,"\t", $y,"\tval=$val\n");
} until ($val >= $max);

print($x,"\t", $y,"\tval=$val\n");
print("steps=",abs($x-1000) + abs($y-1000), "\n");

