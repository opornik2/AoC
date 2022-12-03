#!/usr/bin/python3

import sys

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

start = int(t[0])
end = start
buses = list(t[1].split(','))

while True:
    for b in buses:
        if b != 'x' and end % int(b) == 0:
            diff = end - start
            busid = int(b) * diff
            print(f"end: {end}")
            print(f"diff: {diff}")
            print(f"busid: {busid}")
            sys.exit(0)
    end += 1


