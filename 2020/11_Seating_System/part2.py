#!/usr/bin/python3

import sys
import copy

b = []
c = []

def occupied(m,n):
    global b
    count = 0
    maxx = len(b)
    maxy = len(b[m])
    way = [[-1,0], [1,0], [-1,-1], [0,-1], [1,-1], [-1,1], [0,1], [1,1] ]
    #print("m=%i  n=%i  b[x][y]=%s" % (m,n,b[n][m]))
    for k,l in way:
        #print("k=%i  l=%i" % (k,l))
        x = m
        y = n
        while x+k >=0 and x+k <maxx and y+l >=0 and y+l <maxy:
            #print("x+k=%i  y+l=%i  b[x+k][y+l]=%s" % (x+k,y+l,b[x+k][y+l]))
            x += k
            y += l
            if (b[x][y] == '#' or b[x][y] == 'e'):
                count += 1
                #print("found "+str(b[x][y]))
                break
            elif (b[x][y] == 'L' or b[x][y] == 'o'):
                break
    #print("x=%i  y=%i  count=%i" % (m,n,count))
    return count


with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

#b is t split into 2-dimensional list
b=[list(row) for row in t]


n = 0
while True:
    #make a copy of list for future comparison
    c = copy.deepcopy(b)

    #traverse
    for x in range(len(b)):
        for y in range(len(b[x])):
            if b[x][y] == 'L' and occupied(x,y) == 0:
                b[x][y] = 'o'
            if b[x][y] == '#' and occupied(x,y) >= 5:
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
    #input("Press a key")
    if c == b:

        print("stages: ", n)
        o = 0
        for x in range(len(b)):
            o += b[x].count('#')
        print("occupied: ", o)
        sys.exit(0)

        
