#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], mode='r') as input:
    inp = input.read()

inp = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''
    
summ = 0
t = re.findall(r'mul\(\d+,\d+\)', inp)
for line in t:
    v = re.findall(r'\d+', line)
    summ += int(v[0]) * int(v[1])
    
print(summ)
