#!/usr/bin/python3

import sys
from time import sleep
from math import floor
from itertools import permutations
from queue import Queue
import threading

debug = False
qin = Queue()
qout = Queue()

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().split(",")
prog_list = list(map(int, t))
mem = {i: prog_list[i] for i in range(0, len(prog_list))}   #change list to dict due to access to any element


def intcomp():
    t = mem.copy()
    cursor = 0
    output = None
    rel_base = 0
    while(1):
        opcode = t[cursor] % 100
        mode = []
        mode = list(map(int, str(floor(t[cursor] / 100))))
        mode.reverse()
        for i in range(0,3):
            try: mode[i]
            except: mode.append(0)
        # opcode modes: 0=position mode (index), 1=immediate mode (value), 2=relative mode
        if debug:
            print("\naddr=%d: opcode=%d, p1_mode=%d, p2_mode=%d, p3_mode=%d | " % (cursor, opcode, mode[0], mode[1], mode[2]), end='')
        try:
            if mode[0] == 0: addr1 = t.get(cursor+1, 0)
            if mode[0] == 1: addr1 = cursor+1
            if mode[0] == 2: addr1 = t.get(cursor+1, 0) + rel_base

            if mode[1] == 0: addr2 = t.get(cursor+2, 0)
            if mode[1] == 1: addr2 = cursor+2
            if mode[1] == 2: addr2 = t.get(cursor+2, 0) + rel_base

            if mode[2] == 0: addr3 = t.get(cursor+3, 0)
            if mode[2] == 1: addr3 = cursor+3
            if mode[2] == 2: addr3 = t.get(cursor+3, 0) + rel_base
        except: pass

        #if debug: input()

        if opcode == 1: # add a+b
            t[addr3] = t.get(addr1, 0) + t.get(addr2, 0)
            if debug: print("%i+%i -> %i(%i)" %(t.get(addr1, 0), t.get(addr2, 0), addr3, t[addr3]))
            cursor += 4

        elif opcode == 2: # multiply a*b
            t[addr3] = t.get(addr1, 0) * t.get(addr2, 0)
            if debug: print("%i*%i -> %i(%i)" %(t.get(addr1, 0), t.get(addr2, 0), addr3, t[addr3]))
            cursor += 4

        elif opcode == 3: # store input to addr1
            t[addr1] = qin.get()
            if debug: print("input(%i) saved to mem[%i]" %(t[addr1], addr1))
            cursor += 2

        elif opcode == 4: # output value of addr1
            output = t.get(addr1, 0)
            print(output)
            qout.put(output)
            if debug: print("output: %i" %(output))
            cursor += 2

        elif opcode == 5: # if a<>0 jump to b
            if t.get(addr1, 0) != 0: cursor = t.get(addr2, 0)
            else: cursor += 3
            if debug: print("if %i<>0: goto %i" %(t.get(addr1, 0), t.get(addr2, 0)))

        elif opcode == 6: # if a==0 jump to b
            if t.get(addr1, 0) == 0: cursor = t.get(addr2, 0)
            else: cursor += 3
            if debug: print("if %i==0: goto %i" %(t.get(addr1, 0), t.get(addr2, 0)))

        elif opcode == 7: # if a<b then c=1, else c=0
            if t.get(addr1, 0) < t.get(addr2, 0): t[addr3] = 1
            else: t[addr3] = 0
            if debug: print("if %i<%i: 1|0 -> %i" %(t.get(addr1, 0), t.get(addr2, 0), addr3))
            cursor += 4

        elif opcode == 8: # if a==b c=1, else c=0
            if t.get(addr1, 0) == t.get(addr2, 0): t[addr3] = 1
            else: t[addr3] = 0
            if debug: print("if %i==%i: 1|0 -> %i" %(t.get(addr1, 0), t.get(addr2, 0), addr3))
            cursor += 4

        elif opcode == 9: # adjusts relative base
            if debug: print("rel_base: %i -> %i" %(rel_base, rel_base + t.get(addr1, 0)))
            rel_base += t.get(addr1, 0)
            cursor += 2

        elif opcode == 99: # HALT
            print("HALT output=%i\n" %(output))
            #print("%i" %(output))
            return

        else:
            print("error! instruction at position %i = %i" % (cursor, (t[cursor])))
            sys.exit(1)


panels = [[0 for x in range(200)] for y in range(200)]
x = 100
y = 100
direction = 'n'  #north
coloured = {}

th = threading.Thread(name="intcomp", target=intcomp)
th.start()

while True:
    qin.put(panels[x][y])
    print("x:%i  y:%i" %(x,y))
    colour = qout.get()
    panels[x][y] = colour
    coloured[(x,y)] = 1

    turn = qout.get()
    if direction == 'n':
        if turn == 0:
            x -= 1
            direction = 'w'
        else:
            x += 1
            direction = 'e'
    elif direction == 's':
        if turn == 1:
            x -= 1
            direction = 'w'
        else:
            x += 1
            direction = 'e'
    elif direction == 'e':
        if turn == 0:
            y -= 1
            direction = 'n'
        else:
            y += 1
            direction = 's'
    elif direction == 'w':
        if turn == 1:
            y -= 1
            direction = 'n'
        else:
            y += 1
            direction = 's'
    print("coloured: %i" %(len(coloured.keys())))
    #sleep(0.02)



main_thread = threading.main_thread()
for thread in threading.enumerate():
    if thread is main_thread:
        continue
    th.join()

