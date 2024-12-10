#!/usr/bin/env python3

import sys
from collections import defaultdict
import queue
import numpy

def valid(dest, mh):
    # mh = marker height
    # dh = destination height
    global x
    global y
    
    if dest[0] < 0 or dest[0] >= x: return False  #must fit in the world
    if dest[1] < 0 or dest[1] >= y: return False  #must fit in the world
    if visited[str(dest)] == True: return False
    dh = ord(t[dest[1]][dest[0]])
    if dh == ord('E'): dh = 999
    if dh <= mh+1: return True
    if mh == ord('z') and dh == 999: 
        #print(f"End?? mh={mh}, dest={dest}, dh={dh}")
        return True
    return False
    #print(f"Something went wrong!! mh={mh}, dest={dest}, dh={dh}")


def search():
    marker = q.get()
    step = steps[str(marker)]
    if visited[str(marker)] == True: return False
    else: visited[str(marker)] = True
    # h - current hight
    h = ord(t[marker[1]][marker[0]])
    if h == ord('S'): h = ord('a')
    #print(f"marker= {marker}   h={t[marker[1]][marker[0]]}/{h}   step={step}")
    if h == ord('E'):
        print(f"Finished in {step} steps!")
        return step
    for vector in ([0,1], [0,-1], [1,0], [-1,0]):
        dest = (marker[0]+vector[0], marker[1]+vector[1])
        if not valid(dest, h):
            continue
        #print(f"dest vector: {vector}")
        q.put(dest)
        steps[str(dest)] = step+1

def print_dic(a):
    for r in range(0, maxrow):
        for c in range(0, maxcol):
            try:
                print(a[complex(r,c)], end="")
            except:
                print(" ", end="")
        print()

def grid2cplxdic(grid, ignore_chars=""):
    """
    converts traditional [x(column), y(row)] grid into a dic with inverted coordinates
    based on complex numbers:
    returns: row + col j with their value
    0+0j ----> 0+9j
      |          |
      |          |
    9+0j ----> 9+9j
    """
    dic = {}
    ignore = set(ignore_chars)
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char in ignore: continue
            dic[complex(row, col)] = char
    return dic
    # parsing such dic:  for k, v in dic.items()
##########

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

grid = grid2cplxdic(t)
maxcol = len(t[0])
maxrow = len(t)

# search Startpoints
startpoints = [position for position, height in grid.items() if height == 0]

for line in t:
    m = 0
    for el in line:
        if el == "a":
            q = queue.Queue()
            visited = defaultdict(dict)
            marker = ()
            steps = {}
            marker = (m, n)
            #print(f"Starting at {marker}")
            steps[str(marker)] = 0
            #visited[str(marker)] = True
            q.put(marker)
            while not q.empty():
                #for line in tt:
                #    for el in line:
                #        print(el,end="")
                #    print()
                #input()
                stepsnumber = search()

            #print(f"======================================= empty queue!  steps={stepsnumber}")
        m += 1
    n += 1
