#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split('\n')


total = 0
for line in t:
    (p1,p2) = line.split(",")
    (a,b) = p1.split("-")
    (c,d) = p2.split("-")
    if (int(a) >= int(c) and int(b) <= int(d)):
        print(line+"   (p1)", end="")
        total += 1
    elif (int(c) >= int(a) and int(d) <= int(b)):
        print(line+"   (p2)", end="")
        total += 1
    print()
print(str(total))

