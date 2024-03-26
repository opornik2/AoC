#!/usr/bin/env python3

import sys
import re

def boxnum(step):
    hash = 0
    for char in step:
        if ord(char) < 97: continue
        hash += ord(char)
        hash *= 17
        hash %= 256
    #print(f"{y}\t{step}\t{hash}")
    return hash

def findlens(box, step):
    try:
        for i, lens in enumerate(box):
            if step.split("=")[0] == lens.split("=")[0]:
                box[i] = step
                return 1
        return 0
    except:
        return 0


with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split(",")

summ = 0
boxes = {}   # dic with key = boxnum, value = list of lenses names
for y, step in enumerate(t):
    box = boxnum(step)
    if "=" in step:
        try: 
            if not findlens(boxes[box], step):
                boxes[box].append(step)
        except: 
            boxes[box] = list()
            boxes[box].append(step)
    else:   # "-" in step
        try:
            for lens in boxes[box]:
                if step.replace("-", "") == lens.split("=")[0]:
                    boxes[box].remove(lens)
        except: pass

for box, lenses in boxes.items():
    for i, lens in enumerate(lenses):
        focal = int(lens.split("=")[1])
        power = (box+1) * (i+1) * focal
        summ += power


print(summ)
