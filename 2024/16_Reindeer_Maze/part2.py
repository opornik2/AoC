#!/usr/bin/env python3
import sys
import time
from heapq import heapify, heappop, heappush

debug = True if "debug" in sys.argv else False
grid = dict()
visited = set()
score = {}
dirchar = {-1:"^", 1j:">", 1:"v", -1j:"<"}
recur = 0

# ----------------------------------------------------
class Graph:
    ''' based on https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python
    and corrected by ChatGPT! '''
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
    global recur
    recur += 1
    if debug: print(f"recur: {recur}")
    visited.add(cursor)
    for dire in [1j, 1, -1j, -1]:
        neib = cursor + dire
        try:
            if not "#" in grid[neib]:
                if debug: print(f"{dirchar[curdire]} {cursor} {dirchar[dire]}\t{neib}")
                scoring = 1 if curdire == neib-cursor else 1001
                if debug: print(f"scoring={scoring}")
                #G.add_edge(cursor, cursor+dire)

                if neib not in visited:
                    DFS(neib)
        except: pass
    recur -= 1


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
                    G.add_edge(cursor, neib)
                    if neib not in visited:
                        visited.add(neib)
                        if neib != endpoint:
                            q.append( (neib, dire) )
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
G = Graph()
BFS(startpoint)
#DFS(startpoint)
print(score[endpoint])
print(G.shortest_path(startpoint, endpoint))

###
print(f"Elapsed time: {time.time() - start_time:.4f} seconds")
