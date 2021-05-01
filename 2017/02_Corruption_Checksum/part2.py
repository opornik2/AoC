#!/usr/bin/env python3

import sys
t = []
mem = 0
dziel = 0.0

with open('input', mode='r') as input:
    for line in input:
        t = list(map(int, line.split('\t')))
        for ela in t:
            for elb in t:
                if ela == elb:
                    continue
                if ela % elb == 0:
                    mem += ela/elb
                    break

print("result = " + str(mem))
sys.exit(0)

