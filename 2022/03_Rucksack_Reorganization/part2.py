#!/usr/bin/env python3

import sys

with open('input', mode='r') as input:
    t = input.read().strip().split('\n')


def point(x):
    if ord(x) > 90: return ord(x)-96  #a-z
    else: return ord(x)-38            #A-Z


total = 0
group = 0
dic = {}
for line in t:
    group += 1
    if group > 3: group = 1

    if group == 1:
        for e in line: dic[e] = 1
    elif group == 2:
        for e in line:
            try:
                dic[e]
                dic[e] = 2
            except: continue
    else:
        for e in line:
            try: 
                if dic[e] == 2:
                    total += point(e)
                    dic = {}
                    print(e)
                    break
            except:
                continue

print(str(total))

