#!/usr/bin/env python3
import sys

summ = 0
part = 1
space_w = 101
space_h = 103
start = []
end = []
duration = 100
summ = 1

quadrants = [ ( (0,0), (int((space_w-1)/2)-1, int((space_h-1)/2)-1)),
      ( (int((space_w-1)/2)+1, 0), (space_w-1, int((space_h-1)/2)-1)),
      ( (0, int((space_h-1)/2)+1), (int((space_w-1)/2)-1, space_h-1)),
      ( (int((space_w-1)/2)+1, int((space_h-1)/2)+1), (space_w-1, space_h-1))
     ]

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

for i, l in enumerate(t):
    pos = eval(l.split(" ")[0].replace("p=","")) # eval makes a tuple (x,y) from string "x,y"
    vel = eval(l.split(" ")[1].replace("v=",""))
    start.append( (pos, vel) )

for pair in start:
    (pos, vel) = pair
    newpos_x = (pos[0] + duration * vel[0]) % space_w
    newpos_y = (pos[1] + duration * vel[1]) % space_h
    end.append( (newpos_x, newpos_y) )

for q in quadrants:
    robots = 0
    for r in end:
        if q[0][0] <= r[0] <= q[1][0] and q[0][1] <= r[1] <= q[1][1]:
            robots += 1
    summ *= robots

print(summ)

