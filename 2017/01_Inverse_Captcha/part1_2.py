#!/usr/bin/env python3

import sys
t = ""

with open('input', mode='r') as input:
    t = str(input.read().strip())

index = 0
mem = 0
ahead = 1

for e in t:
   if e == t[(index+ahead) % len(t)]:
        mem += int(e)
   index += 1

print("result = " + str(mem))
sys.exit(0)

