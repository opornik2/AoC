#!/usr/bin/env python3

import sys

with open('input', mode='r') as input:
    t = input.read().strip().split('\n')


def point(x):
    if ord(x) > 90: return ord(x)-96  #a-z
    else: return ord(x)-38            #A-Z


total = 0
for line in t:
    left = line[:int(len(line)/2)]
    right = line[int(len(line)/2):]
    dic = {}
    for e in left:
        dic[e] = True
    for e in right:
        try: 
            dic[e]
            total += point(e)
            break
        except:
            continue
print(str(total))

