#!/usr/bin/python3
# https://hunt.reaktor.com/nanobots

import sys
import re
import itertools

t = {}

with open(sys.argv[1], mode='r') as inputfile:
    byte = inputfile.read(1)
    while byte:
        #print(byte)
        try:
            t[byte] += 1
        except:
            t[byte] = 1
        byte = inputfile.read(1)

{print(k,end="") for k, v in sorted(t.items(), reverse=True, key=lambda item: item[1])}
