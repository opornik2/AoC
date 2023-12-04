#!/usr/bin/env python3

import sys
import re
from collections import defaultdict

def find_gear(row, col):
    global max_rows
    global max_cols
    global gear
    sym = '[*]'
    if row > 0 and col > 0:
        match = re.search(sym, t[row-1][col-1])
        if match != None: return f"{row-1}-{col-1}"
    if col > 0:
        match = re.search(sym, t[row][col-1])
        if match != None: return f"{row}-{col-1}"
    if row < max_rows-1 and col > 0:
        match = re.search(sym, t[row+1][col-1])
        if match != None: return f"{row+1}-{col-1}"
    if row > 0:
        match = re.search(sym, t[row-1][col])
        if match != None: return f"{row-1}-{col}"
    if row < max_rows-1:
        match = re.search(sym, t[row+1][col])
        if match != None: return f"{row+1}-{col}"
    if row > 0 and col < max_cols-1:
        match = re.search(sym, t[row-1][col+1])
        if match != None: return f"{row-1}-{col+1}"
    if col < max_cols-1:
        match = re.search(sym, t[row][col+1])
        if match != None: return f"{row}-{col+1}"
    if row < max_rows-1 and col < max_cols-1:
        match = re.search(sym, t[row+1][col+1])
        if match != None: return f"{row+1}-{col+1}"

    return False



with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")
max_rows = len(t)
max_cols = len(t[0])
partno_l = []
summ = 0
partid = False
gear = {}

for row, line in enumerate(t):
    print(line)
    for col, el in enumerate(line):
        print(f"{row},{col}")
        print(el)
        if el.isdigit():
            partno_l.append(el)
            gear_pos = find_gear(row, col)
            if gear_pos != False:
                partid = True
                try: gear[gear_pos]
                except: gear[gear_pos] = 1
        if col == max_cols-1 or not t[row][col+1].isdigit():
            if len(partno_l) > 0:
                partno = int("".join(partno_l))
                if gear_pos != False:
                    gear[gear_pos] *= partno
                partno_l=[]
                if partid == True:
                    summ += gear[gear_pos]
                    partid = False
                    gear_pos=""
                    print(partno)

print(summ)

