#!/usr/bin/python3

import sys
import math

debug = False
moon = []
statezero = []
moon.append({'x':-1, 'y':0, 'z':2, 'vx':0, 'vy':0, 'vz':0})
moon.append({'x':2,  'y':-10, 'z':-7, 'vx':0, 'vy':0, 'vz':0})
moon.append({'x':4, 'y':-8, 'z':8,  'vx':0, 'vy':0, 'vz':0})
moon.append({'x':3, 'y':5, 'z':-1,  'vx':0, 'vy':0, 'vz':0})

for q in range(0,4):
    statezero.append(moon[q].copy())

def velocity(g,h):
    if g < h: return 1
    elif g > h: return -1
    else: return 0


def calc(dim, vel):
    step = 0
    while True:
        if step % 100000 == 0:
            print("%s step %i" %(dim,step))
            printstate()
        match = 0
        for q in range(0,4):
            if moon[q][dim] == statezero[q][dim] and moon[q][vel] == statezero[q][vel] and step > 1:
                match += 1
            else:
                break
        if match == 4:
            print("After %i steps" % (step))
            printstate()
            return step

        for a in range(0,4):
            for b in range(0,4):
                if a == b: continue
                moon[a][vel] += velocity(moon[a][dim], moon[b][dim])
        for a in range(0,4):
            moon[a][dim] += moon[a][vel]
        step += 1

def printstate():
    for q in range(0,4):
        print("x:%i\ty:%i\tz:%i\t\tvx:%i\tvy:%i\tvz:%i" %(moon[q]['x'], moon[q]['y'], moon[q]['z'], moon[q]['vx'], moon[q]['vy'], moon[q]['vz']))

def nww(a,b):
    return (a*b) // math.gcd(a,b)

printstate()
steps_x = calc('x', 'vx')
steps_y = calc('y', 'vy')
steps_z = calc('z', 'vz')
nww1 = nww2 = 0
nww1 = nww(steps_x, steps_y)
nww2 = nww(steps_z, nww1)
print("output: %i" % (nww2))

