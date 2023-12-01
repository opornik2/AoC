#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

summ = 0
for l in t:
    print(l)
    digits=[]
    while True:
        if l=="": break
        digit = 0
        pat = '^\d'
        if re.search(pat, l):
            match = re.search(pat, l)
            digit = int(match.group(0))
        elif re.search('^one', l):
            digit = 1
        elif re.search('^two', l):
            digit = 2
        elif re.search('^three', l):
            digit = 3
        elif re.search('^four', l):
            digit = 4
        elif re.search('^five', l):
            digit = 5
        elif re.search('^six', l):
            digit = 6
        elif re.search('^seven', l):
            digit = 7
        elif re.search('^eight', l):
            digit = 8
        elif re.search('^nine', l):
            digit = 9
        l = l[1:]
        if digit > 0:
            digits.append(digit)
    digit1 = digits[0]
    digit2 = digits[-1]
    summ += 10*int(digit1) + int(digit2)
print(summ)
