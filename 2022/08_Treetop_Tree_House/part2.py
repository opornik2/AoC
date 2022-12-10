#!/usr/bin/env python3

import sys

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split('\n')

#t = list(map(int, t))
r = c = score = highscore = 0

for r in range(1, len(t)-1):   #row
    for c in range(1, len(t[r])-1):   #column
        e = int(t[r][c])   #element value - tree hight
        distance = [0,0,0,0]

        for k in range(c-1, -1, -1):  #checking left direction
            distance[0] += 1
            v = int(t[r][k])    #cursor value
            print(f"r={r}  c={c}  e={e}  |  r={r}  k={k}  v={v}")
            if v >= e:
                break
        for k in range(c+1, len(t[c]), 1):  #checking right direction
            distance[1] += 1
            v = int(t[r][k])    #cursor value
            print(f"r={r}  c={c}  e={e}  |  r={r}  k={k}  v={v}")
            if v >= e:
                break

        for k in range(r-1, -1, -1):  #checking up direction
            distance[2] += 1
            v = int(t[k][c])    #cursor value
            print(f"r={r}  c={c}  e={e}  |  k={k}  c={c}  v={v}")
            if v >= e:
                break

        for k in range(r+1, len(t[r]), 1):  #checking down direction
            distance[3] += 1
            v = int(t[k][c])    #cursor value
            print(f"r={r}  c={c}  e={e}  |  k={k}  c={c}  v={v}")
            if v >= e:
                break

        score = distance[0] * distance[1] * distance[2] * distance[3]
        print(f"score={score}")
        if score > highscore: highscore = score

print(f"highscore={highscore}")

