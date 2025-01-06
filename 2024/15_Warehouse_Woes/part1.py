#!/usr/bin/env python3

import sys

debug = 0
dirs = {"^": -1, "v": 1, ">": 1j, "<": -1j}
rev = {-1: "^", 1: "v", 1j: ">", -1j: "<"}
cursor = 0
summ = 0

def move_obstacle(obstacle, direction):
    if debug: print(f"O {rev[direction]}")
    try:
        if grid[obstacle + direction] == "#": return False    #next is wall
        elif grid[obstacle + direction] == ".":         #next is empty
            grid[obstacle] = "."
            obstacle += direction
            grid[obstacle] = "O"
            return True
        else:   #next is Obstacle
            if move_obstacle(obstacle + direction, direction) == False:
                return False
            else:
                return True
    except: 
        print("Error1 !!!????")
        return   #next is out of grid, should not happen as we have wall around

def go(direction):
    global cursor
    if debug: print(f"@ {rev[direction]}")
    if grid[cursor + direction] == "#": return
    elif grid[cursor + direction] == ".":
        grid[cursor] = "."
        cursor += direction
        grid[cursor] = "@"
        return
    else:  #there is an Obstacle in the way
        if move_obstacle(cursor + direction, direction):
            go(direction)
        else:
            return


def print_dic(a):
    for r in range(maxrow):
        for c in range(maxcol):
            print(a[complex(r,c)], end="")
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
            #dic[row, col] = char
    return dic
    # parsing such dic:  for k, v in dic.items()

##########

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip()

grid, movements = t.split("\n\n")
t = grid.split("\n")
movements = movements.replace("\n", "")
maxcol = len(t[0])
maxrow = len(t)
grid = grid2cplxdic(t)

#find start
for k, v in grid.items():
    if v == "@":
        cursor = k
        break

print_dic(grid)
for m in movements:
    go(dirs[m])
    if debug: print_dic(grid)


for k, v in grid.items():
    if v == "O":
        summ += int(100*k.real + k.imag)

print(summ)