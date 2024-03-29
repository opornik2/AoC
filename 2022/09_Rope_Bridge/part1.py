#!/usr/bin/env python3

import sys
from collections import defaultdict

def rope(t,h):
    return max(abs(t[0]-h[0]), abs(t[1]-h[1]))


def right(steps):
    seen[t[0]][t[1]] = 1
    for s in range(1, steps+1):
        h[0] += 1
        if rope(h,t) > 1:
            t[0] += 1   # if too long
            if t[1] != h[1]: t[1] = h[1]  #if diagonal
        seen[t[0]][t[1]] = 1

def left(steps):
    seen[t[0]][t[1]] = 1
    for s in range(1, steps+1):
        h[0] -= 1
        if rope(h,t) > 1:
            t[0] -= 1   # if too long
            if t[1] != h[1]: t[1] = h[1]  #if diagonal
        seen[t[0]][t[1]] = 1

def up(steps):
    seen[t[0]][t[1]] = 1
    for s in range(1, steps+1):
        h[1] += 1
        if rope(t,h) > 1:
            t[1] += 1
            if t[0] != h[0]: t[0] = h[0]
        seen[t[0]][t[1]] = 1

def down(steps):
    seen[t[0]][t[1]] = 1
    for s in range(1, steps+1):
        h[1] -= 1
        if rope(t,h) > 1:
            t[1] -= 1   # if not covering
            if t[0] != h[0]: t[0] = h[0]  #if diagonal
        seen[t[0]][t[1]] = 1


with open(sys.argv[1], mode='r') as input:
    fi = input.read().strip().split('\n')

h = [0,0]
t = [0,0]
seen = defaultdict(dict)
count = 0

for line in fi:
    (dire, steps) = line.split(" ")
    steps = int(steps)
    if dire == "R": right(steps)
    elif dire == "D": down(steps)
    elif dire == "L": left(steps)
    elif dire == "U": up(steps)
    print(f"H={h[0]}.{h[1]}  T={t[0]}.{t[1]}")

for k in seen.keys():
    for n in seen[k].keys():
        print(f"{n}.{k}")
        count += 1
print(f"count={count}")
