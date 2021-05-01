#!/usr/bin/python3

import sys

debug = False
moon = []
moon.append({'x':16, 'y':-8, 'z':13, 'vx':0, 'vy':0, 'vz':0})
moon.append({'x':4,  'y':10, 'z':10, 'vx':0, 'vy':0, 'vz':0})
moon.append({'x':17, 'y':-5, 'z':6,  'vx':0, 'vy':0, 'vz':0})
moon.append({'x':13, 'y':-3, 'z':0,  'vx':0, 'vy':0, 'vz':0})

#moon.append({'x':-1, 'y':0,   'z':2,  'vx':0, 'vy':0, 'vz':0})
#moon.append({'x':2,  'y':-10, 'z':-7, 'vx':0, 'vy':0, 'vz':0})
#moon.append({'x':4,  'y':-8,  'z':8,  'vx':0, 'vy':0, 'vz':0})
#moon.append({'x':3,  'y':5,   'z':-1, 'vx':0, 'vy':0, 'vz':0})


def velocity(g,h):
    if g < h: return 1
    elif g > h: return -1
    else: return 0

totalenergy = 0
for step in range(0,1001):
    print("After %i steps" % (step))
    for q in range(0,4):
        if step > 0: print("x:%i\ty:%i\tz:%i\t\tvx:%i\tvy:%i\tvz:%i\t\tener:%i" %(moon[q]['x'], moon[q]['y'], moon[q]['z'], moon[q]['vx'], moon[q]['vy'], moon[q]['vz'], moon[q]['ener']))
    print("total energy: %i" %(totalenergy))
    if debug: input()
    for a in range(0,4):
        for b in range(0,4):
            if a == b: continue
            moon[a]['vx'] += velocity(moon[a]['x'], moon[b]['x'])
            moon[a]['vy'] += velocity(moon[a]['y'], moon[b]['y'])
            moon[a]['vz'] += velocity(moon[a]['z'], moon[b]['z'])
    totalenergy = 0
    for a in range(0,4):
        moon[a]['x'] += moon[a]['vx']
        moon[a]['y'] += moon[a]['vy']
        moon[a]['z'] += moon[a]['vz']
        moon[a]['pot'] = abs(moon[a]['x']) + abs(moon[a]['y']) + abs(moon[a]['z'])
        moon[a]['kin'] = abs(moon[a]['vx']) + abs(moon[a]['vy']) + abs(moon[a]['vz'])
        moon[a]['ener'] = moon[a]['pot'] * moon[a]['kin']
        totalenergy += moon[a]['ener']

