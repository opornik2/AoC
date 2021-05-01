cat modules |perl -ne'$a=int($_/3)-2;$sum+=$a; print "$sum\n"' | tail -1
