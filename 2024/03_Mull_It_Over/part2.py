#!/usr/bin/env python3

import sys
import re

with open(sys.argv[1], mode='r') as input:
    inp = input.read()

#inp = '''xmul(2,4)%&mul[3,7]!@^don't()_mul(5,5)+mul(32,64]then(mul(11,8)undo()?mul(8,5))'''

summ = 0
u = re.sub(r"don't\(\).+?do\(\)", '', inp, flags=re.DOTALL)

t = re.findall(r'mul\(\d+,\d+\)', u)
for line in t:
    #print(line)
    v = re.findall(r'\d+', line)
    summ += int(v[0]) * int(v[1])
    
print(summ)
    
