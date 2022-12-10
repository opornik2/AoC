#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split('\n')

#t = list(map(int, t))
r = c = visible = maxx = 0

for r in range(1, len(t)-1):   #row
    for c in range(1, len(t[r])-1):   #column
        e = int(t[r][c])   #element value - tree hight

        for k in range(c-1, -1, -1):  #checking left direction
            v = int(t[r][k])    #cursor value
            print(f"r={r}  c={c}  e={e}  |  r={r}  k={k}  v={v}")
            clear = True
            if v >= e:
                clear = False
                break
        if clear:
            visible += 1
            continue

        for k in range(c+1, len(t[c]), 1):  #checking right direction
            v = int(t[r][k])    #cursor value
            print(f"r={r}  c={c}  e={e}  |  r={r}  k={k}  v={v}")
            clear = True
            if v >= e:
                clear = False
                break
        if clear:
            visible += 1
            continue

        for k in range(r-1, -1, -1):  #checking up direction
            v = int(t[k][c])    #cursor value
            print(f"r={r}  c={c}  e={e}  |  k={k}  c={c}  v={v}")
            clear = True
            if v >= e:
                clear = False
                break
        if clear:
            visible += 1
            continue

        for k in range(r+1, len(t[r]), 1):  #checking down direction
            v = int(t[k][c])    #cursor value
            print(f"r={r}  c={c}  e={e}  |  k={k}  c={c}  v={v}")
            clear = True
            if v >= e:
                clear = False
                break
        if clear:
            visible += 1
            continue

visible = visible + 2*len(t[0]) + 2*len(t) - 4
print(f"visible={visible}")

