#!/usr/bin/python3

import sys
import re

debug = False
counter = 0

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().split('\n\n')

for group in t:
    ans = {}
    group = group.strip()
    group = re.sub(r'\n', '', group)
    for el in group:
        ans[el] = 1
    counter += len(ans)
    print(len(ans))

print(counter)
