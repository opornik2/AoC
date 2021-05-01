#!/usr/bin/python3

import sys
import re

debug = False
counter = 0

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().split('\n\n')

for group in t:
    ans = {}
    men = 0
    group = group.strip()
    person = group.split('\n')
    for p in person:
        for el in p:
            try: ans[el] += 1
            except: ans[el] = 1
        men += 1
    for k in ans:
        if ans[k] == men:
            counter += 1
    print(counter)


