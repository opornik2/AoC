#!/usr/bin/env python3
import sys
from time import sleep

space_w = maxrow = 101
space_h = maxcol = 103
start = []
duration = 200000
grid = dict()


def print_dic(a):
    for r in range(maxrow):
        for c in range(maxcol):
            print(a[complex(r,c)], end="")
        print()

##############################################################################################

for y in range(space_h):
    for x in range(space_w):
        grid[complex(x,y)] = "."

with open(sys.argv[1], mode='r') as fh:
    t = fh.read().strip().split("\n")

for i, l in enumerate(t):
    pos = eval(l.split(" ")[0].replace("p=","")) # eval makes a tuple (x,y) from string "x,y"
    vel = eval(l.split(" ")[1].replace("v=",""))
    start.append( (pos, vel) )

#print_dic(grid)

for n in range(duration):
    grid2 = grid.copy()
    for pair in start:
        (pos, vel) = pair
        newpos_x = (pos[0] + n * vel[0]) % space_w
        newpos_y = (pos[1] + n * vel[1]) % space_h
        grid2[complex(newpos_x, newpos_y)] = "@"
    
    if sum(1 for k,v in grid2.items() if k.imag==maxcol-1 and v=="@") > 0:
        continue
    print_dic(grid2)
    print(n)
    input()
    #sleep(0.4)

