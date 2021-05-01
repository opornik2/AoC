#!/usr/bin/python3

import sys
import re

debug = False
counter = 0
seat = {}
i = 1000

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().split('\n')

for line in t:
    line = line.strip()
    try:
        row = line[0:7]
        column = line[7:10]
        row = re.sub(r'F', '0', row)
        row = re.sub(r'B', '1', row)
        row = int('0b' + row, 2)
        column =  re.sub(r'L', '0', column)
        column =  re.sub(r'R', '1', column)
        column = int('0b' + column, 2)
        id = row*8 + column
        seat[id] = 1
        if id < i:
            i = id
    except:
        print(line)


for k, v in seat.items():
    if k != i:
        print(i)
        break
    i += 1


