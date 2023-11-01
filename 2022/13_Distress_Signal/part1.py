#!/usr/bin/env python3

import sys
from collections import defaultdict
#import numpy
import json
#visited = defaultdict(dict)

def parse_packet(line, l):
    l = json.loads(line)
    return l

def comp_lists(a, b):
    global o_sum
    print(a)
    print(b)
    ordered = 1
    if len(a)>0 and len(b)==0: return 0
    for i in range(0, len(b)):
        if ordered==0: return 0
        if ordered==2: return 2
        try: a[i]
        except: return 2

        if isinstance(a[i], int) and isinstance(b[i], int):
            if a[i] < b[i]:
                return 2
            elif a[i] > b[i]:
                return 0
        elif isinstance(a[i], list) and isinstance(b[i], list):
            ordered = comp_lists(a[i], b[i])
        else:
            if isinstance(a[i], int):
                ordered = comp_lists([a[i]], b[i])
            else:
                ordered = comp_lists(a[i], [b[i]])

    return ordered


pair = 0
o_sum = 0
with open(sys.argv[1], mode='r') as infile:
    while True:
        pair += 1
        try:
            a = json.loads(infile.readline().strip())
            b = json.loads(infile.readline().strip())
            try: infile.readline()
            except: break
            ordered = comp_lists(a, b)
            if ordered == 2: o_sum += pair
            print(f"pair {pair} = {ordered}\n")
        except: break

print(o_sum)
sys.exit

