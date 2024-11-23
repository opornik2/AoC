#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode='r') as infile:
     t = infile.read().strip().split("\n")

diff1 = diff2 = 0
for line in t:
    lenstring = len(line)
    exec(f"mem = {line}")
    lenmemory = len(mem)
    #x = line.encode('utf-8')
    diff1 += lenstring - lenmemory
    #encoded = repr(lenstring)
    print(line)
    line = line.replace('\\', '\\\\')
    print(line)
    line = line.replace("\"", "\\\"")
    print(line)
    lenencoded = len(line) + 2
    diff2 += lenencoded - lenstring
print(diff1)
print(diff2)
