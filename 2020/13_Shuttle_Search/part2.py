#!/usr/bin/python3

import sys

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

start = 100000000000011
buses = list(t[1].split(','))

while True:
    idx = 0
    match = 0
    for b in buses:
        if b != 'x':
            c = start+idx
            b = int(b)
            d = c % b
            if d == 0:
                match += 1
            else:
                break
        idx += 1
    print(match)
    if match == len(buses)-1:
        print(start)
        sys.exit(0)
    start += 23
    print(start)
