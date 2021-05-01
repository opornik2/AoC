#!/usr/bin/python3

import sys
from math import floor
from itertools import permutations
from queue import Queue
import threading

phases = [9,8,7,5,6]
debug = True

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().split(",")
prog_list = list(map(int, t))
mem = {i: prog_list[i] for i in range(0, len(prog_list))}   #change list to dict due to access to any element


def intcomp(inp, ampno):
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
            try:
                t[addr1] = inp.pop(0)
            except:
                t[addr1] = q[ampno].get()
            #if debug:
            #    print("\nI'm amp[%i]" %(ampno))
            if debug: print("input(%i) saved to mem[%i]" %(t[addr1], addr1))
            cursor += 2

        elif opcode == 4: # output value of addr1
            output = t.get(addr1, 0)
            #q[(ampno+1) % 5].put(output)
            print(output)
            if debug: print("output[amp%i]: %i" %(ampno, output))
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

results = []
q = []
for i in range(0,5): q.append(Queue())
q[0].put(1)
intcomp(0,0)
sys.exit(0)

for ph in list(permutations(phases)):
    q = []
    for i in range(0,5):
        q.append(Queue())
    if debug:
        print("phases:" + str(ph))
    for amp in range(0,5):
        inputs = []
        inputs.append(ph[amp])  # first input to Amplifier
        if amp == 0:
            inputs.append(0)   # second input only to ampA
        x = threading.Thread(name="amp"+str(amp), target=intcomp, args=(inputs, amp))
        x.start()

    main_thread = threading.main_thread()
    for x in threading.enumerate():
        if x is main_thread:
            continue
        x.join()
    #print("output = %i\n" % (result))
    #results.append(result)  # let's make a list of all results
    #sys.exit(0)


#print(max(results))


