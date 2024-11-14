#!/usr/bin/env python3

import sys
import re

cnt = 0

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

for line in t:
    print(line)
    match = re.search(r"(.)(?=\1)", line)
    if match != None:
        match =  re.findall(r"([aeiou])", line)
        if len(match) >= 3:
            match =  re.search(r"(ab|cd|pq|xy)", line)
            if match == None:
                cnt += 1
                print ("OK")

print (cnt)

