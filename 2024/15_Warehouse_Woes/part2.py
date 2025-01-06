#!/usr/bin/env python3

import sys

debug = 1 if "debug" in sys.argv else 0

dirs = {"^": -1, "v": 1, ">": 1j, "<": -1j}
rev = {-1: "^", 1: "v", 1j: ">", -1j: "<"}
cursor = 0
summ = 0
q = []


def make_chain(cursor, direction):
    if grid[cursor] == "@":
        if grid[cursor + direction] == "[":
            q.append(cursor + direction)
            make_chain(cursor + direction, direction)
        elif grid[cursor + direction] == "]":
            q.append(cursor + dirs["<"] + direction)
            make_chain(cursor + dirs["<"] + direction, direction)
        return
    elif grid[cursor] == "[":
        if cursor not in q: q.append(cursor)
        make_chain(cursor + direction, direction)
        make_chain(cursor + dirs[">"] + direction, direction)
    elif grid[cursor] == "]":
        if cursor + dirs["<"] not in q: q.append(cursor + dirs["<"])
        make_chain(cursor + direction, direction)
        make_chain(cursor + dirs["<"] + direction, direction)
    return

def check_movable(direction):
    while len(q) > 0:
        obstacle = q.pop()
        if grid[obstacle + direction] == "#" or grid[obstacle + dirs[">"] + direction] == "#":
            return False    #next is wall
    return True

def move_obstacle(obstacle, direction):
    if debug: print(f"{grid[obstacle]} {rev[direction]}")
    try:
        if direction == dirs["<"] or direction == dirs[">"]:   #moving < >
            if grid[obstacle + direction] == "#": return False    #next is wall
            elif grid[obstacle + direction] == ".":         #next is empty
                symbol = grid[obstacle]
                grid[obstacle] = "."
                obstacle += direction
                grid[obstacle] = symbol
                return True
            else:   #next is Obstacle
                if move_obstacle(obstacle + direction, direction) == False:
                    return False
                else:
                    return True
        else:                                    #moving ^ V
            if grid[obstacle] == "[":
                if grid[obstacle + direction] == "#" or grid[obstacle + dirs[">"] + direction] == "#":
                    return False    #next is wall
                elif grid[obstacle + direction] == "." and grid[obstacle + dirs[">"] + direction] == ".":  #next is empty
                    grid[obstacle] = "."
                    grid[obstacle + dirs[">"]] = "."
                    grid[obstacle + direction] = "["
                    grid[obstacle + dirs[">"] + direction] = "]"
                    return True
                else:   #next is Obstacle
                    if grid[obstacle + direction] != ".":
                        if move_obstacle(obstacle + direction, direction) ==  False:
                            return False
                        else:
                            return True
                    else:
                        if move_obstacle(obstacle + dirs[">"] + direction, direction) ==  False:
                            return False
                        else:
                            return True

            else: # we are at ]
                if grid[obstacle + direction] == "#" or grid[obstacle + dirs["<"] + direction] == "#":
                    return False    #next is wall
                elif grid[obstacle + direction] == "." and grid[obstacle + dirs["<"] + direction] == ".":  #next is empty
                    grid[obstacle] = "."
                    grid[obstacle + dirs["<"]] = "."
                    grid[obstacle + direction] = "]"
                    grid[obstacle + dirs["<"] + direction] = "["
                    return True
                else:   #next is Obstacle
                    if grid[obstacle + direction] != ".":
                        if move_obstacle(obstacle + direction, direction) == False:
                            return False
                        else:
                            return True
                    else:
                        if move_obstacle(obstacle + dirs["<"] + direction, direction) == False:
                            return False
                        else:
                            return True


    except: 
        print("Error1 !!!????")
        return   #next is out of grid, should not happen as we have wall around

def go(direction):
    global cursor
    q.clear()
    if debug: print(f"@ {rev[direction]}")
    if grid[cursor + direction] == "#": return
    elif grid[cursor + direction] == ".":
        grid[cursor] = "."
        cursor += direction
        grid[cursor] = "@"
        return
    else:  #there is an Obstacle in the way
        if direction == dirs["<"] or direction == dirs[">"]:   #moving < >
            if move_obstacle(cursor + direction, direction):
                go(direction)
            else:
                return
        else:  #moving ^ v
            make_chain(cursor, direction) #stores obstacles in a queqe
            if check_movable(direction):  #check if all obstacles from the quque can move
                move_obstacle(cursor + direction, direction)
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

with open(sys.argv[1], mode='r') as inp:
    t = inp.read().strip()

grid, movements = t.split("\n\n")
#extend the grid
if not "[" in grid:
    grid = grid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")

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
    if v == "[":
        summ += int(100*k.real + k.imag)

print(summ)