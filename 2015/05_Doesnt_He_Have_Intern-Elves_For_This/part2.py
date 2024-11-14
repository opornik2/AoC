#!/usr/bin/env python3

import sys
import re

cnt = 0

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

for line in t:
    print(line)
    match = re.search(r"(..).*(?=\1)", line)
    if match != None:
        match =  re.search(r"(.).(?=\1)", line)
        if match != None:
            cnt += 1
            print ("OK")

print (cnt)

