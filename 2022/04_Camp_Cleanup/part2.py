#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split('\n')


total = 0
for line in t:
    print(line)
    dic = {}
    (p1,p2) = line.split(",")
    (a,b) = p1.split("-")
    (c,d) = p2.split("-")
    for i in range(int(a), int(b)+1):
        dic[i] = True
    for k in range(int(c), int(d)+1):
        try:
            dic[k]
            total += 1
            print(k)
            break
        except: pass

print(str(total))

