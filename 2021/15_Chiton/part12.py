#!/usr/bin/env python3
import sys
import time
from heapq import heapify, heappop, heappush

debug = True if "debug" in sys.argv else False
grid = dict()
dirchar = {-1:"^", 1j:">", 1:"v", -1j:"<"}
recur = 0
visited = set()

# ----------------------------------------------------
class Graph:
    ''' from https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python '''
    def __init__(self, graph: dict = {}):
        self.graph = graph  # A dictionary for the adjacency list

    def add_edge(self, node1, node2, weight=1):
        if node1 not in self.graph:  # Check if node already added
            self.graph[node1] = {}  # If not, create the node
        self.graph[node1][node2] = weight  # Else, add a connection to its neighbor

    def shortest_distances(self, source: str):
        # Initialize the distances to all nodes as infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source distance to 0
        
        # Initialize a priority queue
        #With real,imag the priority queue remains valid even when distances are equal
        # priority queue comaprison does not support pure complex numbers
        pq = [(0, (source.real, source.imag))]   # (distance, node)
        #heapify(pq)   #this is actually not needed
        predecessors = {node: None for node in self.graph}
        while pq:  # While the priority queue isn't empty
            current_distance, (real, imag) = heappop(pq)  # Get the node with the min distance
            current_node = complex(real, imag)

            # If the distance in the queue is outdated, skip it
            if current_distance > distances[current_node]:
                continue

            # Relaxation step
            for neib, weight in self.graph[current_node].items():
                # Calculate the distance from current_node to the neib
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neib]:
                    distances[neib] = tentative_distance
                    predecessors[neib] = current_node  # Update predecessor
                    heappush(pq, (tentative_distance, (neib.real, neib.imag)))  #With real,imag the priority queue remains valid even when distances are equal, as '<' not supported between instances of 'complex' and 'complex'
    
        return distances, predecessors

    def shortest_distance(self, source: str, target: str):
        distances, _ = self.shortest_distances(source)
        return distances[target]

    def shortest_path(self, source: str, target: str):
        ''' By using the shortest_distances function, we generate the predecessors dictionary. 
        Then, we start a while loop that goes back a node from the current node in each iteration 
        until the source node is reached. 
        Then, we return the list reversed, which contains the path from the source to the target.'''
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)
        path = []
        current_node = target
        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()
        return path

def DFS(cursor):  # Depth First Search (recursive)
    global recur, visited
    recur += 1
    if debug: print(f"recur: {recur}")
    visited.add(cursor)
    for dire in [1j, 1, -1j, -1]:
        neib = cursor + dire
        try: grid[neib]
        except KeyError: continue
        if debug: print(f"{cursor} {dirchar[dire]}\t{neib}")
        G.add_edge(cursor, neib, grid[neib])
        if neib not in visited:
            DFS(neib)
    recur -= 1

def BFS(cursor):  # Breadth First Search (iteration)
    _visited = set()
    curdire = 1j #East
    q = [(cursor, curdire)]
    _visited.add(cursor)
    while q:
        cursor, curdire = q.pop(0)
        for dire in [-1, 1j, 1, -1j]:
            neib = cursor + dire
            try: grid[neib]
            except KeyError: continue
            if debug: print(f"{dirchar[curdire]} {cursor} {dirchar[dire]}\t{neib}")
            G.add_edge(cursor, neib, grid[neib])
            if neib not in _visited:
                _visited.add(neib)
                q.append( (neib, dire) )

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

maxcol = len(t[0])
maxrow = len(t)

grid = grid2cplxdic(t)
grid = { k: int(v) for k,v in grid.items() }
startpoint = 0
endpoint = complex(len(t)-1, len(t[0])-1)
sys.setrecursionlimit(20000)
G = Graph()
BFS(startpoint)
#DFS(startpoint)
if debug: print(G.shortest_path(startpoint, endpoint))
print(G.shortest_distance(startpoint, endpoint))

# part 2 - expand the grid
for y in range(5 * maxrow):
    for x in range(5 * maxcol):
        addition = (x // maxrow + y // maxcol) % 10
        grid[complex(x,y)] = ((grid[complex(x % maxrow, y % maxcol)] + addition - 1) % 9) + 1

maxcol *= 5
maxrow *= 5
endpoint = complex(maxrow-1, maxcol-1)
G = Graph()

BFS(startpoint)
#DFS(startpoint)
if debug: print_dic(grid)
if debug: print(G.shortest_path(startpoint, endpoint))
print(G.shortest_distance(startpoint, endpoint))



###
print(f"Elapsed time: {time.time() - start_time:.4f} seconds")
