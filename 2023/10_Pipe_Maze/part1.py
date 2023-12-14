#!/usr/bin/env python3

import sys
import re

def find_way(posx, posy):
    print(f"{t[posy][posx]} ({posx},{posy})", end="")
    next_pipe(posx, posy)

def next_pipe(posx, posy):
    global steps
    global maxsteps
    if t[posy][posx] == "S" and steps>0:
        maxsteps = steps
        return False
    if (posx,posy) in visited: return False
    visited[(posx,posy)] = True
    tt[posy]=list(tt[posy])
    if t[posy][posx] != "S": tt[posy][posx] = str(steps % 10)
    steps += 1
    print(f"{t[posy][posx]} ({posx},{posy})  steps {steps}")
    try:
        if t[posy][posx] in "S-":
            if right(posx, posy): return True
            if left(posx, posy): return True
        if t[posy][posx] in "S|":
            if down(posx, posy): return True
            if up(posx, posy): return True
        if t[posy][posx] in "SL":
            if right(posx, posy): return True
            if up(posx, posy): return True
        if t[posy][posx] in "SJ":
            if up(posx, posy): return True
            if left(posx, posy): return True
        if t[posy][posx] in "S7":
            if left(posx, posy): return True
            if down(posx, posy): return True
        if t[posy][posx] in "SF":
            if down(posx, posy): return True
            if right(posx, posy): return True
        return False
    except:
        return False

def right(posx, posy):
    if t[posy][posx+1] in "-7JS":
        if next_pipe(posx+1, posy):
            return True
def left(posx, posy):
    if t[posy][posx-1] in "-FLS":
        if next_pipe(posx-1, posy):
            return True
def down(posx, posy):
    if t[posy+1][posx] in "|JLS":
        if next_pipe(posx, posy+1):
            return True
def up(posx, posy):
   if t[posy-1][posx] in "|7FS":
        if next_pipe(posx, posy-1):
            return True

steps = 0
maxsteps = 0
cur_pos = []  #cursor
visited = {}
print(sys.setrecursionlimit(50000))

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")
tt=t[:]

#find start
for y, line in enumerate(t):
    if "S" in line:
        cur_pos = [line.index("S"), y]
        break

find_way(cur_pos[0], cur_pos[1])
steps = int((maxsteps+1)/2)
print(f"Further steps from S = {steps}")

for line in tt:
    print("".join(line))

