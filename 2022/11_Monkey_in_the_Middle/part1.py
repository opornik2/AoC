#!/usr/bin/env python3

import sys
from collections import defaultdict
import queue
#import numpy

inspect = [0,0,0,0,0,0,0,0]
qu = []
for i in range(0,8):
    qu.append(queue.Queue())

for n in (89, 73, 66, 57, 64, 80):
    qu[0].put(n)
for n in (83, 78, 81, 55, 81, 59, 69):
    qu[1].put(n)
for n in (76, 91, 58, 85):
    qu[2].put(n)
for n in (71, 72, 74, 76, 68):
    qu[3].put(n)
for n in (98, 85, 84):
    qu[4].put(n)
qu[5].put(78)
for n in (86, 70, 60, 88, 88, 78, 74, 83):
    qu[6].put(n)
for n in (81, 58):
    qu[7].put(n)

def proc0():
    global qu
    global inspect
    while not qu[0].empty():
        wl1 = qu[0].get() * 3
        inspect[0] += 1
        wl2 = int(wl1 / 3)
        if ( wl2 % 13 == 0):
            qu[6].put(wl2)
        else:
            qu[2].put(wl2)

def proc1():
    global qu
    global inspect
    while not qu[1].empty():
        wl1 = qu[1].get() + 1
        inspect[1] += 1
        wl2 = int(wl1 / 3)
        if ( wl2 % 3 == 0):
            qu[7].put(wl2)
        else:
            qu[4].put(wl2)

def proc2():
    global qu
    global inspect
    while not qu[2].empty():
        wl1 = qu[2].get() * 13
        inspect[2] += 1
        wl2 = int(wl1 / 3)
        if ( wl2 % 7 == 0):
            qu[1].put(wl2)
        else:
            qu[4].put(wl2)

def proc3():
    global qu
    global inspect
    while not qu[3].empty():
        wl1 = qu[3].get() ** 2
        inspect[3] += 1
        wl2 = int(wl1 / 3)
        if (wl2 % 2 == 0):
            qu[6].put(wl2)
        else:
            qu[0].put(wl2)

def proc4():
    global qu
    global inspect
    while not qu[4].empty():
        wl1 = qu[4].get() + 7
        inspect[4] += 1
        wl2 = int(wl1 / 3)
        if ( wl2 % 19 == 0):
            qu[5].put(wl2)
        else:
            qu[7].put(wl2)

def proc5():
    global qu
    global inspect
    while not qu[5].empty():
        wl1 = qu[5].get() + 8
        inspect[5] += 1
        wl2 = int(wl1 / 3)
        if ( wl2 % 5 == 0):
            qu[3].put(wl2)
        else:
            qu[0].put(wl2)

def proc6():
    global qu
    global inspect
    while not qu[6].empty():
        wl1 = qu[6].get() + 4
        inspect[6] += 1
        wl2 = int(wl1 / 3)
        if ( wl2 % 11 == 0):
            qu[1].put(wl2)
        else:
           qu[2].put(wl2)

def proc7():
    global qu
    global inspect
    while not qu[7].empty():
        wl1 = qu[7].get() + 5
        inspect[7] += 1
        wl2 = int(wl1 / 3)
        if ( wl2 % 17 == 0):
            qu[3].put(wl2)
        else:
            qu[5].put(wl2)


for i in range(1,21):
    print(f"Iteration {i}")
    proc0()
    proc1()
    proc2()
    proc3()
    proc4()
    proc5()
    proc6()
    proc7()

inspect.sort()
out = inspect.pop() * inspect.pop()

print(out)

