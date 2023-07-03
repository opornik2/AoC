#!/usr/bin/env python3

import sys
from collections import defaultdict
import queue
#import numpy

inspect = [0,0,0,0]
qu = []
for i in range(0,4):
    qu.append(queue.Queue())

for n in (79, 98):
    qu[0].put(n)
for n in (54, 65, 75, 74):
    qu[1].put(n)
for n in (79, 60, 97):
    qu[2].put(n)
qu[3].put(74)

def lower_wl(wl1):
    return int(wl1 / 3)

def proc0():
    global qu
    global inspect
    while not qu[0].empty():
        wl1 = qu[0].get() * 19
        print(f'qu0 wl1={wl1}')
        inspect[0] += 1
        wl2 = lower_wl(wl1)
        print(f'qu0 wl2={wl2}')
        if ( wl2 % 23 == 0):
            qu[2].put(wl2)
        else:
            qu[3].put(wl2)

def proc1():
    global qu
    global inspect
    while not qu[1].empty():
        wl1 = qu[1].get() + 6
        print(f'qu1 wl1={wl1}')
        inspect[1] += 1
        wl2 = lower_wl(wl1)
        print(f'qu1 wl2={wl2}')
        if ( wl2 % 19 == 0):
            qu[2].put(wl2)
        else:
            qu[0].put(wl2)

def proc2():
    global qu
    global inspect
    while not qu[2].empty():
        wl1 = qu[2].get() ** 2
        print(f'qu2 wl1={wl1}')
        inspect[2] += 1
        wl2 = lower_wl(wl1)
        print(f'qu2 wl2={wl2}')
        if ( wl2 % 13 == 0):
            qu[1].put(wl2)
        else:
            qu[3].put(wl2)

def proc3():
    global qu
    global inspect
    while not qu[3].empty():
        wl1 = qu[3].get() + 3
        print(f'qu3 wl1={wl1}')
        inspect[3] += 1
        wl2 = lower_wl(wl1)
        print(f'qu3 wl2={wl2}')
        if (wl2 % 17 == 0):
            qu[0].put(wl2)
        else:
            qu[1].put(wl2)

#####

print(f"Iteration {i}")
proc0()
proc1()
proc2()
proc3()

for i in range(0,4):
    print(f'monkey {i}: {inspect[i]}')

for i in range(2,21):
    print(f"Iteration {i}")
    proc0()
    proc1()
    proc2()
    proc3()

for i in range(0,4):
    print(f'monkey {i}: {inspect[i]}')

#inspect.sort()
#out = inspect.pop() * inspect.pop()
#print(out)
