#!/usr/bin/env python3

import sys
import re
from collections import defaultdict

def find_symbol(row, col):
    global max_rows
    global max_cols
    sym = '[^0-9.]'
    if row > 0 and col > 0:
        match = re.search(sym, t[row-1][col-1])
        if match != None: return True
    if col > 0:
        match = re.search(sym, t[row][col-1])
        if match != None: return True
    if row < max_rows-1 and col > 0:
        match = re.search(sym, t[row+1][col-1])
        if match != None: return True
    if row > 0:
        match = re.search(sym, t[row-1][col])
        if match != None: return True
    if row < max_rows-1:
        match = re.search(sym, t[row+1][col])
        if match != None: return True
    if row > 0 and col < max_cols-1:
        match = re.search(sym, t[row-1][col+1])
        if match != None: return True
    if col < max_cols-1:
        match = re.search(sym, t[row][col+1])
        if match != None: return True
    if row < max_rows-1 and col < max_cols-1:
        match = re.search(sym, t[row+1][col+1])
        if match != None: return True
    return False



with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")
max_rows = len(t)
max_cols = len(t[0])
partno_l = []
summ = 0
partid = False

for row, line in enumerate(t):
    #print(line)
    for col, el in enumerate(line):
        #print(f"{row},{col}")
        #print(el)
        if el.isdigit():
            partno_l.append(el)
            if find_symbol(row, col):
                partid = True
        if col == max_cols-1 or not t[row][col+1].isdigit():
            if len(partno_l) > 0:
                partno = int("".join(partno_l))
                partno_l=[]
                if partid == True:
                    summ += partno
                    partid = False
                    print(partno)

print(summ)

