#!/usr/bin/env python3

import sys
from collections import defaultdict
import queue
import numpy

def valid(dest, h):
    global x
    global y
    if visited[str(dest)] == True: return False
    if 0 <= dest[0] < y and 0 <= dest[1] < x:
        if h <= ord(t[dest[1]][dest[0]]) <= h+1: return True
        elif h == ord('z') and ord(t[dest[1]][dest[0]]) == ord('E'): return True
    return False

def search():
    marker = q.get()
    step = steps[str(marker)]
    if visited[str(marker)] == True: return False
    else: visited[str(marker)] = True
    if t[marker[1]][marker[0]] == "S": h = ord('a')
    else: h = ord(t[marker[1]][marker[0]])
    print(f"marker= {marker}   h={t[marker[1]][marker[0]]}/{h}   step={step}")
    if h == ord('E'):
        print(f"Finished, step={step}")
        sys.exit(0)
    for vector in ([0,1], [0,-1], [1,0], [-1,0]):
        dest = (marker[0]+vector[0], marker[1]+vector[1])
        if not valid(dest, h):
            continue
        q.put(dest)
        steps[str(dest)] = step+1

with open(sys.argv[1], mode='r') as infile:
     t = infile.read().strip().split('\n')

#tt = numpy.zeros((len(t[0]),len(t)))
q = queue.Queue()
start=[10,10]
end=[10,10]
visited = defaultdict(dict)
marker = ()
steps = {}
x = y = 0
for line in t:
    if "S" in line:
        for el in line:
            #tt[x][y] = el
            if el == "S":
                start[0] = x
                start[1] = y
                break
        x += 1
    y += 1
x = len(t[0])
y = len(t)
marker = (start[0], start[1])
steps[str(marker)] = 0
#visited[str(marker)] = True
q.put(marker)
while not q.empty():
    #for line in tt:
    #    for el in line:
    #        print(el,end="")
    #    print()
    #input()
    search()

print("ERROR: empty queue!")
