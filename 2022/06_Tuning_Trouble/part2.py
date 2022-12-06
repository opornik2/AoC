#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip()

cnt = 0
lst = []
for e in t:
    cnt += 1
    lst.append(e)
    if len(lst) > 14: lst = lst[1:]
    if len(lst) == 14:
        k = 0
        for i in range(0, 14):
            if lst.count(lst[i]) > 1:
                break
            else:
                k += 1
        if k == 14:
            print(str(cnt))
            sys.exit()

