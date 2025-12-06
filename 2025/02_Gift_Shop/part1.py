#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split(",")

summ=0
for line in t:
    (start, end) = line.split("-")
    # naive bruteforce for all numbers in all ranges
    for el in range(int(start),int(end)+1):
        if len(str(el))%2 == 0:
            half = len(str(el))//2
            if str(el)[0:half] == str(el)[half:]:
                summ += el

print(summ)
