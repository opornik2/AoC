#!/usr/bin/env python3

import sys
t = []
linepassed = 0
counter = 0

with open('input', mode='r') as input:
    for line in input:
        t = list(line.split(' '))
        passes = {}
        for pas in t:
            if not pas.strip() in passes:
                passes[pas.strip()] = 1
                linepassed = 1
            else:
                linepassed = 0
                break
        counter += linepassed

print("result = " + str(counter))
sys.exit(0)

