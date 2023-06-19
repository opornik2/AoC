#!/usr/bin/env python3

import sys
from collections import defaultdict

def right():
    print(">")
    marker[0] += 1
    marker[2] = t[marker[1]][marker[0]]
    visited[str(marker[:2])] = True
    find_next(marker)

def down():
    print("V")
    marker[1] += 1
    marker[2] = t[marker[1]][marker[0]]
    visited[str(marker[:2])] = True
    find_next(marker)

def left():
    print("<")
    marker[0] -= 1
    marker[2] = t[marker[1]][marker[0]]
    visited[str(marker[:2])] = True
    find_next(marker)

def up():
    print("^")
    marker[1] -= 1
    marker[2] = t[marker[1]][marker[0]]
    visited[str(marker[:2])] = True
    find_next(marker)

def find_next(marker):
    global steps
    steps += 1
    cur_h = ord(marker[2])
    print(f"marker= {marker}   steps={steps}")
    try:
        if ord(t[marker[1]+1][marker[0]]) == cur_h+1 \
            and marker[1]+1 < y \
            and visited[str([marker[0], marker[1]+1])] != True: #look down
            down()
    except: pass
    try:
        if ord(t[marker[1]-1][marker[0]]) == cur_h+1 \
            and marker[1]-1 >=0 \
            and visited[str([marker[0], marker[1]-1])] != True: #look up
            up()
    except: pass
    try:
        if (ord(t[marker[1]][marker[0]+1]) == cur_h+1 or ord(t[marker[1]][marker[0]+1]) == ord('E')) \
            and marker[0]+1 < x \
            and visited[str([marker[0]+1, marker[1]])] != True: #look right
            right()
    except: pass
    try:
        if (ord(t[marker[1]][marker[0]-1]) == cur_h+1 or ord(t[marker[1]][marker[0]-1]) == ord('E')) \
            and marker[0]-1 >=0 \
            and visited[str([marker[0]-1, marker[1]])] != True: #look left
            left()
    except: pass
    try:
        if ord(t[marker[1]+1][marker[0]]) == cur_h \
            and marker[1]+1 < y \
            and visited[str([marker[0], marker[1]+1])] != True: #look down
            down()
    except: pass
    try:
        if ord(t[marker[1]-1][marker[0]]) == cur_h \
            and marker[1]-1 >=0 \
            and visited[str([marker[0], marker[1]-1])] != True: #look up
            up()
    except: pass
    try:
        if ord(t[marker[1]][marker[0]+1]) == cur_h \
            and marker[0]+1 < x \
            and visited[str([marker[0]+1, marker[1]])] != True: #look right
            right()
    except: pass
    try:
        if ord(t[marker[1]][marker[0]-1]) == cur_h \
            and marker[0]-1 >=0 \
            and visited[str([marker[0]-1, marker[1]])] != True: #look left
            left()
    except: pass
    return marker


with open(sys.argv[1], mode='r') as infile:
     t = infile.read().strip().split('\n')

start=[10,10]
end=[10,10]
marker = [0, 0, 'a']
visited = defaultdict(dict)
visited[str(marker[:2])] = True
steps = -1
x = y = 0
for line in t:
    if "S" in line:
        for el in line:
            if el == "S":
                start[0] = x
                start[1] = y
                break
        x += 1
    y += 1
x = len(t[0])
y = len(t)
marker[0] = start[0]
marker[1] = start[1]
new = [0, 0, 'S']
new = find_next(marker)
