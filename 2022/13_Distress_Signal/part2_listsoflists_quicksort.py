#!/usr/bin/env python3

import sys
from collections import defaultdict
#import numpy
import json
#visited = defaultdict(dict)


def quicksort(k):
    left=[]
    right=[]
    pivot=k.pop()
    for el in k:
        #if el <= pivot: left.append(el)   # this would be for
        #else: right.append(el)            # standard numeric comaprison
        if comp_lists(el, pivot) == 2: left.append(el)      # this is for our
        else: right.append(el)                              # lists of lists comparison
    if len(left)>1: left=quicksort(left)
    if len(right)>1: right=quicksort(right)
    ksorted=left + [pivot] + right
    return ksorted


def parse_packet(line, l):
    l = json.loads(line)
    return l

def comp_lists(a, b):
    global o_sum
    #print(a)
    #print(b)
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

k = [[[2]],[[6]]]
with open(sys.argv[1], mode='r') as infile:
    t = [line.strip() for line in infile]

for l in t:
    if l != "":
        k.append(json.loads(l))

ksorted=quicksort(k)
#for el in ksorted: print(el)
for idx, line in enumerate(ksorted):
    print(f'{idx+1}   {line}')
    try:
        if len(line)==1 and len(line[0])==1:
            if line[0][0] == 2: x = idx+1
            elif line[0][0] == 6: y = idx+1
    except: pass
print(int(x)*int(y))

