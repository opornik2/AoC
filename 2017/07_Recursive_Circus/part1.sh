cat input | cut -f1 -d' ' > 01
for n in `cat 01`; do echo -n "$n = "; grep -c $n input; done | grep 1

rm -f 01
