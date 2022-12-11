#!/usr/bin/env python3

import sys
from collections import defaultdict
import math

def dist(t,h):
    return max(abs(t[0]-h[0]), abs(t[1]-h[1]))


def col_round(x):
    if x >= 0.0:
        return math.floor(x + 0.5)
    else:
        return math.ceil(x - 0.5)

def draw(): 
    box = 15
    for i in range(100+box, 100-box-1, -1):
        for j in range(100-box, 100+box+1):
            char = "•"
            for n in range(knots-1, -1, -1):
                try:
                    if r[n][0]==j and r[n][1]==i:
                        char = str(n)
                        if n==0: char = "H"
                except:
                    pass
            if i==100 and j==100: char = "s"
            print(char, end="")
        print("\n")
    print("\n")


###############################################################################


with open(sys.argv[1], mode='r') as infile:
    fi = infile.read().strip().split('\n')

seen = defaultdict(dict)
count = 0
knots = 10
tail = knots-1
r = []
for i in range(0, knots):
    r.append([100,100])

for line in fi:
    print(f"\nline: {line}")
    #print(f"before {r}")
    (dire, steps) = line.split(" ")
    steps = int(steps)
    seen[r[tail][0]][r[tail][1]] = 1
    for _ in range(1, steps+1):
        if dire   == "R": r[0][0] += 1
        elif dire == "L": r[0][0] -= 1
        elif dire == "U": r[0][1] += 1
        elif dire == "D": r[0][1] -= 1
        for knot in range(1,knots):
            di = dist(r[knot-1], r[knot])
            #print(f"dist  {knot-1}-{knot} = {di}")
            if di > 1:
                r[knot][0] += col_round((r[knot-1][0] - r[knot][0])/2)
                r[knot][1] += col_round((r[knot-1][1] - r[knot][1])/2)
        #print(f"middle {r}")
        seen[r[tail][0]][r[tail][1]] = 1
        draw()
        #input()

    #print(f"after  {r}")

for k in seen.keys():
    for n in seen[k].keys():
        print(f"{n}.{k}")
        count += 1
print(f"count={count}")
