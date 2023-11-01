#!/usr/bin/env python3

import sys
from collections import defaultdict
import json

def parse_packet(line, l):
    l = json.loads(line)
    return l


with open(sys.argv[1], mode='r') as infile:
    t = infile.read().strip().split('\n')

lines = []
for line in t:
    if line == "": continue
    lines.append(line.replace("[","").replace("]","").replace(",",""))

#lines.append("2")
#lines.append("6")

for idx, line in enumerate(sorted(lines)):
    print(f'{idx}   {line}')
    if line == "2":
        x = idx+1
    elif line == "6":
        y = idx+1

print(int(x)*int(y))

