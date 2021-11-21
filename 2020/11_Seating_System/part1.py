#!/usr/bin/python3

import sys
import copy

b = []
c = []

def occupied(x,y):
    global b
    n = 0
    maxx = len(b)-1
    maxy = len(b[x])-1
    if x>0 and ( b[x-1][y] == '#' or b[x-1][y] == 'e'): n += 1
    if x<maxx and (b[x+1][y] == '#' or b[x+1][y] == 'e'): n += 1
    if x>0 and y>0 and (b[x-1][y-1] == '#' or b[x-1][y-1] == 'e'): n += 1
    if y>0 and (b[x][y-1] == '#' or b[x][y-1] == 'e'): n += 1
    if x<maxx and y>0 and (b[x+1][y-1] == '#' or b[x+1][y-1] == 'e'): n += 1
    if x>0 and y<maxy and (b[x-1][y+1] == '#' or b[x-1][y+1] == 'e'): n += 1
    if y<maxy and (b[x][y+1] == '#' or b[x][y+1] == 'e'): n += 1
    if x<maxx and y<maxy and (b[x+1][y+1] == '#' or b[x+1][y+1] == 'e'): n += 1
    return n


with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

#split into 2-dimensional list
for x in range(len(t)):
    b.append(list(t[x]))


n = 0
while True:
    #make a copy of list for future comparison
    c = copy.deepcopy(b)
    #traverse
    for x in range(len(b)):
        for y in range(len(b[x])):
            if b[x][y] == 'L' and occupied(x,y) == 0:
                b[x][y] = 'o'
            if b[x][y] == '#' and occupied(x,y) >= 4:
                b[x][y] = 'e'
            #print(b[x][y], end='')
        #print("\n", end='')
    #print("\n", end='')

    for x in range(len(b)):
        for y in range(len(b[x])):
            if b[x][y] == 'o':
                b[x][y] = '#'
            if b[x][y] == 'e':
                b[x][y] = 'L'
            print(b[x][y], end='')

        print("\n", end='')
    print("\n", end='')
    n += 1
    if c == b:

        print("stages: ", n)
        o = 0
        for x in range(len(b)):
            o += b[x].count('#')
        print("occupied: ", o)
        sys.exit(0)

        
