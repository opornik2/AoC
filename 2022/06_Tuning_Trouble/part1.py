#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip()

cnt = 0
lst = []
for e in t:
    cnt += 1
    print(e)
    lst.append(e)
    if len(lst) > 4:
        lst = lst[1:]
    if len(lst) == 4:
        if lst.count(lst[0]) == 1 and lst.count(lst[1]) == 1 and lst.count(lst[2]) == 1:
            startofpacket = cnt
            break

print(str(startofpacket))

