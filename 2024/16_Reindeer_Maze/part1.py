#!/usr/bin/env python3
import sys
import time

debug = True if "debug" in sys.argv else False
grid = dict()
visited = set()
score = {}
dirchar = {-1:"^", 1j:">", 1:"v", -1j:"<"}


# ----------------------------------------------------
def BFS(cursor):  # Breadth First Search (iteration)
    curdire = 1j #East
    q = [(cursor, curdire)]
    visited.add(cursor)
    while q:
        cursor, curdire = q.pop(0)
        for dire in [-1, 1j, 1, -1j]:
            neib = cursor + dire
            try:
                if not "#" in grid[neib]:
                    if debug: print(f"{dirchar[curdire]} {cursor} {dirchar[dire]}\t{neib}")
                    scoring = 1 if curdire == neib-cursor else 1001
                    if debug: print(f"scoring={scoring}")
                    try: 
                        score[neib]
                        if debug: print(f"{neib} scoring exists={score[neib]}")
                        if score[cursor] + scoring < score[neib]:
                            score[neib] = score[cursor] + scoring
                            for d in [-1, 1j, 1, -1j]:
                                if (neib, d) in q: q.remove( (neib, d) )
                            q.append((neib, dire))
                            if debug: print(f"{neib} new scoring={score[neib]}")
                    except:
                        score[neib] = score[cursor] + scoring
                    if debug: print(score[neib])
                    if neib not in visited:
                        visited.add(neib)
                        if neib != endpoint: q.append( (neib, dire) )
            except: pass

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

############################################################################

start_time = time.time()
###

with open(sys.argv[1], mode='r') as inp:
    t = inp.read().strip().split("\n")

grid = grid2cplxdic(t)
startpoint = [ k for k, v in grid.items() if v == "S" ][0]
endpoint = [ k for k, v in grid.items() if v == "E" ][0]
score[startpoint] = 0
BFS(startpoint)
print(score[endpoint])


###
print(f"Elapsed time: {time.time() - start_time:.3f} seconds")
