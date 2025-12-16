import sys
import math

def countdist(p1, p2):
    return math.sqrt( (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2 )
    

with open(sys.argv[1], mode='r') as input:
    t = input.read().rstrip("\n").split("\n")

points = []    #list of tuples
circuits = []  #list of sets
dist = {}      #dict of tuple:float

for line in t:
    (x,y,z) = map(int, line.split(","))
    points.append( (x,y,z) )

for p1 in range(len(points)-1):
    min_dist = 9999999999
    for p2 in range(p1+1, len(points)):
        if p1 == p2:
            continue
        dist[ (p1,p2) ] = countdist(points[p1], points[p2])  #dict of tuples

for i, p in enumerate(points):
    circuits.append({i})

n = 0
distances = sorted(dist.items(), key=lambda x:x[1])
for i in range(30):
    print(f"distances: {distances[i]}")

for k, v in distances:
    print(f"points {k} = {v}")
    # condition for counting part 1
    if n == int(sys.argv[2]):
        size = []
        for c in circuits:
            size.append(len(c))

        size.sort(reverse=True)
        print(f"part1: {size[0] * size[1] * size[2]}")
    # condition for counting part 2
    if len(circuits) == 1:
        print(f"{p1}={points[p1]}, {p2}={points[p2]}")
        print(f"part1: {points[p1][0] * points[p2][0]}")
        break

    (p1, p2) = k
    newc = set()
    merged = False
    oldc = []
    for c in circuits:
        if p1 in c and p2 in c:
            continue
        if p1 in c or p2 in c:
            newc |= c   #union with other found circuits
            newc.add(p1)
            newc.add(p2)
            oldc.append(c)
            merged = True
    if merged:
        for c in oldc:
            circuits.remove(c)
        circuits.append(newc)
        print(f"{p1} - {p2}")
        print(f"connections {n}\tdist={v}\n")
    n += 1   # this is nonsense, as already connected points (p1 and p2 in c) should not be counted as new connection!

#print(circuits)

