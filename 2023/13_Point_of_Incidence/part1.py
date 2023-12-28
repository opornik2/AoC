#!/usr/bin/env python3

import sys
import re

summ = 0

def array_transform(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

def sublist(lst1, lst2):
    ls1 = [element for element in lst1 if element in lst2]
    ls2 = [element for element in lst2 if element in lst1]
    return ls1 == ls2

def print_array(a):
    for l in a:
        print(*l)

def find_mirror(grid):
    global summ
    seen = []
    for i in range(0,len(grid)-1):
        if grid[i] == grid[i+1]:
            seen = grid[i::-1]
            rest = grid[i+1:]
            if len(seen) < len(rest):
                diff = [ j for j in range(0, len(seen)) if seen[j]==rest[j] ]
            else:
                diff = [ j for j in range(0, len(rest)) if seen[j]==rest[j] ]
            if len(diff) == min(len(seen), len(rest)):
                axis = i+1
                print(f"axis={axis}")
                #print_array(reversed(seen))
                #print("---")
                #print_array(rest)
                return axis
    return 0

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n\n")

for pattern in t:
    grid = []
    for line in pattern.split("\n"):
        #grid.append(line)      #creates list of strings
        grid.append(list(line)) #creates list of lists
    print("by column")
    summ += find_mirror(array_transform(grid))
    print("by line")
    summ += find_mirror(grid) * 100

print(summ)

