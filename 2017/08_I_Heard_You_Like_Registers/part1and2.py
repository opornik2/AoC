#!/usr/bin/env python3

import sys
t = ""
r = {}
max_r = 0

def comp(reg, op, val):
    global r
    val = int(val)
    if op == '==' and r[reg] == val:
        return True
    elif op == '!=' and r[reg] != val:
        return True
    elif op == '>' and r[reg] > val:
        return True
    elif op == '>=' and r[reg] >= val:
        return True
    elif op == '<' and r[reg] < val:
        return True
    elif op == '<=' and r[reg] <= val:
        return True

    return False


with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split('\n')

for l in t:
    k = l.split(' ')
    #print(k)
    try:    r[k[4]]
    except: r[k[4]] = 0
    try:    r[k[0]]
    except: r[k[0]] = 0
    #print r[k[0]]
    if comp(k[4], k[5], k[6]):
        if k[1] == 'inc':
            r[k[0]] += int(k[2])
        elif k[1] == 'dec':
            r[k[0]] -= int(k[2])
    if r[k[0]] > max_r:
        max_r =  r[k[0]]

for k, v in sorted(r.items(), key=lambda p:p[1]):
    print(k, v)

print("max r = ", max_r)
