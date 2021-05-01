#!/usr/bin/env python3

import sys
t = ""

with open('input', mode='r') as input:
    t = input.read().strip().split('\n')

k = list(map(int, t))
i = 0
steps = 0
#print(k)

while (True):
    val = k[i]
    print('k['+str(i)+']='+str(val))
    k[i] += 1
    i += val
    steps += 1
    #print(k)
    print("steps="+str(steps)+"\n")
    try:
        k[i]
    except:
        break


