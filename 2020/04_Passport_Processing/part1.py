#!/usr/bin/python3

import sys
import re

debug = False
counter = 0

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().split('\n\n')

for line in t:
    p = {}
    line = re.sub(r'\n', ' ', line)
    line = line.strip()
    for element in line.split(' '):
        (field, val) = element.split(':')
        p[field] = val
    try:
        if p['byr'] and p['iyr'] and p['eyr'] and p['hgt'] and p['hcl'] and p['ecl'] and p['pid']:
            counter += 1
    except:
        pass

print(counter)

