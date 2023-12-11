#!/usr/bin/env python3

import sys
import re
from collections import Counter

summ = 0

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

for line in t:
    his = []
    his.append(list(map(int, line.split())))
    i = 0
    while True:
        if his[i].count(his[i][0]) == len(his[i]): break
        his.append([])
        for k in range(1, len(his[i])):
            his[i+1].append(his[i][k] - his[i][k-1])
        i += 1
    print("=====")
    [print(el) for el in his]

    if len(his[i]) < 2: break   # cannot extrapolate if we have only one value in the lowest sequence
    x = his[i][0]
    while True:
        his[i-1].insert(0, his[i-1][0] - x)
        i -= 1
        x = his[i][0]
        print(f"{x}   ")
        if i == 0: break
    summ += x


print(f"Sum={summ}")

