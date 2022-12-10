#!/usr/bin/env python3

import sys
from collections import defaultdict

def dist(t,h):
    return max(abs(t[0]-h[0]), abs(t[1]-h[1]))


def right(knot):
    r[knot][0] += 1   # if > 2 then move right
    if r[knot][1] != r[knot-1][1]:  # if y != Y then Y equal to n-1
        r[knot][1] = r[knot-1][1]  #if diagonal


def left(knot):
    r[knot][0] -= 1   # if too long
    if r[knot][1] != r[knot-1][1]:
        r[knot][1] = r[knot-1][1]  #if diagonal


def up(knot):
    r[knot][1] += 1   # if too long
    if r[knot][0] != r[knot-1][0]:
        r[knot][0] = r[knot-1][0]  #if diagonal


def down(knot):
    r[knot][1] -= 1   # if too long
    if r[knot][0] != r[knot-1][0]:
        r[knot][0] = r[knot-1][0]  #if diagonal


###############################################################################


with open(sys.argv[1], mode='r') as input:
    fi = input.read().strip().split('\n')

r = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
seen = defaultdict(dict)
count = 0

for line in fi:
    print(f"\nline: {line}")
    #print(f"before {r}")
    (dire, steps) = line.split(" ")
    steps = int(steps)
    seen[r[9][0]][r[9][1]] = 1
    for _ in range(1, steps+1):
        if dire   == "R": r[0][0] += 1
        elif dire == "L": r[0][0] -= 1
        elif dire == "U": r[0][1] += 1
        elif dire == "D": r[0][1] -= 1
        for knot in range(1,10):
            di = dist(r[knot-1], r[knot])
            print(f"dist  {knot-1}-{knot} = {di}")
            if dist(r[knot-1], r[knot]) > 1:
                if dire   == "R": right(knot)
                elif dire == "L": left(knot)
                elif dire == "U": up(knot)
                elif dire == "D": down(knot)
        print(f"middle {r}")
        seen[r[9][0]][r[9][1]] = 1
    #print(f"after  {r}")

for k in seen.keys():
    for n in seen[k].keys():
        print(f"{n}.{k}")
        count += 1
print(f"count={count}")
