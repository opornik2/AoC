#!/usr/bin/env python3

import sys
import re
import numpy as np

def print_array(grid):
    for row in range(0, max_rows):
        for col in range(0, max_cols):
            print(grid[row,col], end="")
        print()
    print()

def print_column(grid, col):
    for row in range(0, max_rows):
        print(grid[row,col])

def count_loadN(grid):
    load = 0
    for row in range(0, max_rows):
        for col in range(0, max_cols):
            if grid[row,col] == "O":
                load += max_rows-row
    return load

def grid2dic(grid, ignore_chars=""):
    """
    converts traditional [x(column), y(row)] grid into a dic with inverted coordinates
    
    returns 2-tuples of (row, col) with their value
    (0, 0) ----> (0, 9)
      |            |
      |            |
    (9, 0) ----> (9, 9)
    """
    dic = {}
    ignore = set(ignore_chars)
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char in ignore: continue
            dic[row, col] = char
    return dic
    
    # parsing such dic:  for k, v in dic.items()

def tiltN(grid):
    for col in range(0, max_cols):
        while True:
            #print_column(grid, col)
            moves = 0
            for row in range(1, max_rows):    
                if grid[row, col] == "O" and grid[row-1, col] == ".":
                    grid[row-1, col] = "O"
                    grid[row, col] = "."
                    moves += 1
            if moves == 0:
                break

def tiltS(grid):
    for col in range(0, max_cols):
        while True:
            #print_column(grid, col)
            moves = 0
            for row in range(max_rows-2, -1, -1):    
                if grid[row, col] == "O" and grid[row+1, col] == ".":
                    grid[row+1, col] = "O"
                    grid[row, col] = "."
                    moves += 1
            if moves == 0:
                break

def tiltW(grid):
    for row in range(0, max_rows):
        while True:
            #print_column(grid, col)
            moves = 0
            for col in range(1, max_cols):    
                if grid[row, col] == "O" and grid[row, col-1] == ".":
                    grid[row, col-1] = "O"
                    grid[row, col] = "."
                    moves += 1
            if moves == 0:
                break

def tiltE(grid):
    for row in range(0, max_rows):
        while True:
            #print_column(grid, col)
            moves = 0
            for col in range(max_cols-2, -1, -1):    
                if grid[row, col] == "O" and grid[row, col+1] == ".":
                    grid[row, col+1] = "O"
                    grid[row, col] = "."
                    moves += 1
            if moves == 0:
                break

def load(grid):
    s = 0
    for i, line in enumerate(grid):
        s += np.count_nonzero(line=="O") * (len(grid) - i)
    return s

######################################################################

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

max_rows=len(t)
max_cols=len(t[0])

dic_grid = grid2dic(t)
hist = list()
hist.append(dict(dic_grid))
cycles = 1000000000
print(f"tilt=0, load={count_loadN(dic_grid)}")
for tilt in range(0, cycles):
    tiltN(dic_grid)
    #print_array(dic_grid)
    tiltW(dic_grid)
    #print_array(dic_grid)
    tiltS(dic_grid)
    #print_array(dic_grid)
    tiltE(dic_grid)
    #print_array(dic_grid)
    print(f"tilt={tilt+1}, load={count_loadN(dic_grid)}")
    for h, el in enumerate(hist):
        if dic_grid == el:
            print(f"found a loop: current tilt {tilt+1}")
            loop_elements = tilt+1 - h
            loop_start = tilt - loop_elements + 1
            full_loops = int((cycles-loop_start)/loop_elements)
            hist[0:loop_start] = []
            loop_idx = (cycles - loop_start) - loop_elements*full_loops
            calc_load = count_loadN(hist[loop_idx])
            print(f"loop_start: {loop_start}, loop_elements: {loop_elements}, full_loops: {full_loops}, loop_idx: {loop_idx}")
            print(f"calculated load after all cycles: {calc_load}")
            sys.exit(0)
    hist.append(dict(dic_grid))
