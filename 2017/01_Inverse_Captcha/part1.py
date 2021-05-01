#!/usr/bin/env python3

import sys
t = ""

with open('input', mode='r') as input:
	t = str(input.read().strip())

index = 1
mem = 0
for e in t:
    if index >= len(t):
        if e == t[0]:
            mem += int(e)
        print("result = " + str(mem))
        sys.exit(0)
    if e == t[index]:
        mem += int(e)
    index += 1

