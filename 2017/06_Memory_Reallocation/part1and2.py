#!/usr/bin/env python3

import sys
t = []
x = []

with open('input', mode='r') as input:
    t = list(map(int, input.read().strip().split('\t')))

count = 0
x.append(t[:])

while True:
    #print(t)
    mx = max(t)
    i = 0
    for v in t:
        if v == mx: break
        i += 1
    t[i] = 0
    while mx > 0:
        t[(i+1) % 16] += 1
        mx -= 1
        i += 1
    #print(t)
    #print(x)
    count +=1
    i = 0
    for e in x:
        if e == t:
            print("redistributions=" +str(count))
            print("loop size=" + str(count-i))
            sys.exit(0)
        i += 1
    x.append(t[:])



