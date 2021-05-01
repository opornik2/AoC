cat modules | perl -ne'$mass=$_; $fuel=0; do { $fuel=int($mass/3)-2; $sum+=$fuel; $mass=$fuel; } until ($fuel<9);$suma+=$sum; print "$suma\n";$sum=0;' | tail -1
