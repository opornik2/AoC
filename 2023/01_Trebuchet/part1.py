#!/usr/bin/env python3

import sys
import re

with open('input', mode='r') as input:
    t = input.read().strip().split("\n")

summ=0
for line in t:
    match = re.search('\d', line)
    digit1 = match.group(0)
    match = re.search('\d', line[::-1])
    digit2 = match.group(0)
    summ += 10*int(digit1) + int(digit2)
print(summ)
