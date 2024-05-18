#!/usr/bin/env python3

import sys
import networkx as nx

def move(startpoint):
    next_step = list()
    steps = 0
    for d in -1, 1, 0-1j, 0+1j:
        try:
            if grid[startpoint+d] == '#': continue
        except: 
            continue
        if startpoint+d in visited: continue
        next_step.append(startpoint+d)
    if len(next_step) == 1:
        visited.add(next_step[0])
        move(next_step[0])
    else:
        pass

def find_next_split(cursor):
    global visited
    steps = 0
    while True:
        next_steps = list()
        for d in -1, 1, 0-1j, 0+1j:
            if cursor+d == endpoint:
                G.add_node(cursor, steps=steps)
                return (cursor, [])
            try:
                if grid[cursor+d] == '#': continue
                if grid[cursor+d] == '<' and d == 0+1j: continue
                if grid[cursor+d] == '>' and d == 0-1j: continue
                if grid[cursor+d] == 'v' and d == -1: continue
                if grid[cursor+d] == '^' and d == 1: continue
                
            except: 
                continue
            if cursor+d in visited: continue
            # found at least one corridor
            next_steps.append(cursor+d)
        # checked all 4 directions
        if len(next_steps) == 1:
            cursor = next_steps[0]
            steps += 1
            visited.add(cursor)
            continue
        elif len(next_steps) > 1:
            G.add_node(cursor, steps=steps)
            return (cursor, next_steps)

def print_dic(a):
    for r in range(0, maxrow):
        for c in range(0, maxcol):
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
    return dic
    # parsing such dic:  for k, v in dic.items()
##########

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

grid = grid2cplxdic(t)
visited = set()
maxcol = len(t[0])
maxrow = len(t)
startpoint = 0+1j
endpoint = complex(maxrow, maxcol-1)

G = nx.Graph()
#G.add_node(startpoint, steps=13)   #add new node with attribute
#G.nodes[startpoint]['steps']=13  #node attribute changing
#G.nodes.data()  #display nodes
#G.add_edge(startpoint, endpoint, steps=14 )  #add new edge with attribute
#G.edges[startpoint, endpoint]['steps']=14  #edge attribute changing
#G[startpoint][endpoint]['steps']=14   #also edge attribute changing

G.add_node(startpoint, steps=0)
visited.add(startpoint)
cursor = startpoint
next_steps = []
while True:
    cursor, next_steps = find_next_split(cursor)
    if cursor == endpoint:
        break
    while len(next_steps) > 0:
        cursor = next_steps.pop()
        cursor, next_steps = find_next_split(cursor)


pass
###

#for e in t:
#    p,s  = e.split(')')
#    G.add_edge(p, s)
#    G.nodes[3+12j]['steps']=31
#    G.add_edge(1, 2, weight=4.7 )


#print(list(G.nodes))
#print("\n")
#print(list(G.edges))
#for node in G.successors(root):
#    weight = int(G.nodes[node]['w'])
#    print(node + " " + str(G.nodes[node]['w']))
#    for s in G.successors(node):
#        print("  - " + str(s) + " ("+ str(G.nodes[s]['w'])+")")
#        weight += int(G.nodes[s]['w'])
#    if len(list(G.successors(node))) > 0:
#        #print("total node weight = " + str(weight))
#        print(node + " disk weight = " + str(disk_weight(node)))

#print(nx.shortest_path_length(G, source='YOU', target='SAN')-2)