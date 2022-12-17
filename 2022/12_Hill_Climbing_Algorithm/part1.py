#!/usr/bin/env python3

import sys
from collections import defaultdict



def find_next(marker):
    if t[marker[0]][marker[1] == "E": return
    if ord(h) < ord(marker[2]]:



with open(sys.argv[1], mode='r') as infile:
     t = infile.read().strip().split('\n')

start=[10,10]
end=[10,10]
h = 'a'
marker = [0, 0, 'S']

x = y = 0
for line in t:
    if "S" in line:
        for el in line:
            if el == "S":
                start[0] = x
                start[1] = y
        x += 1
    y += 1
marker[0] = start[0]
marker[1] = start[1]
find_next(marker)
