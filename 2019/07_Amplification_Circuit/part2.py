#!/usr/bin/python3

import sys
from math import floor
from itertools import permutations
from queue import Queue
import threading

phases = [9,8,7,5,6]
debug = False

with open('input', mode='r') as input:
    t = input.read().split(",")
program = list(map(int, t))

#inputs = sys.argv
#inputs.pop(0)  #removes element 0
#inputs = list(map(int, inputs))

def intcomp(inp, ampno):
    t = program[:]
    cursor = 0
    output = None
    while(1):
        opcode = t[cursor] % 100
        mode = []
        mode = list(map(int, str(floor(t[cursor] / 100))))
        mode.reverse()
        for i in range(0,2):
            try: mode[i]
            except: mode.append(0)
        # opcode modes: 0=position mode (index), 1=immediate mode (value)
        if debug:
            print("idx=%d, opcode=%d, 1mode=%d, 2mode=%d | " % (cursor, opcode, mode[0], mode[1]), end='')
        try:
            p1 = t[cursor+1] if mode[0] == 1 else t[t[cursor+1]]
            p2 = t[cursor+2] if mode[1] == 1 else t[t[cursor+2]]
        except: pass

        if opcode == 1: # add a+b
            t[t[cursor+3]] = p1 + p2
            if debug: print("%i+%i -> %i(%i)" %(p1, p2, t[cursor+3], t[t[cursor+3]]))
            cursor += 4

        elif opcode == 2: # multiply a*b
            t[t[cursor+3]] = p1 * p2
            if debug: print("%i*%i -> %i(%i)" %(p1, p2, t[cursor+3], t[t[cursor+3]]))
            cursor += 4

        elif opcode == 3: # store input to a
            try:
                t[t[cursor+1]] = inp.pop(0)
            except:
                t[t[cursor+1]] = q[ampno].get()
            if debug:
                print("\nI'm amp[%i]" %(ampno))
            if debug: print("input(%i) -> %i(%i)" %(t[t[cursor+1]], t[cursor+1], t[t[cursor+1]]))
            cursor += 2

        elif opcode == 4: # output a
            output = t[t[cursor+1]]
            q[(ampno+1) % 5].put(output)
            if debug: print("output[%i]: %i" %(ampno, output))
            cursor += 2

        elif opcode == 5: # if a<>0 jump to b
            if p1 != 0: cursor = p2
            else: cursor += 3
            if debug: print("if %i<>0: goto %i" %(p1, p2))

        elif opcode == 6: # if a==0 jump to b
            if p1 == 0: cursor = p2
            else: cursor += 3
            if debug: print("if %i==0: goto %i" %(p1, p2))

        elif opcode == 7: # if a<b c=1, else c=0
            if p1 < p2: t[t[cursor+3]] = 1
            else: t[t[cursor+3]] = 0
            if debug: print("if %i<%i: 1|0 -> %i" %(p1, p2, t[cursor+3]))
            cursor += 4

        elif opcode == 8: # if a==b c=1, else c=0
            if p1 == p2: t[t[cursor+3]] = 1
            else: t[t[cursor+3]] = 0
            if debug: print("if %i==%i: 1|0 -> %i" %(p1, p2, t[cursor+3]))
            cursor += 4

        elif opcode == 99: # HALT
            #print("HALT output=%i\n" %(output))
            print("%i" %(output))
            return

        else:
            print("error! instruction at position %i = %i" % (cursor, (t[cursor])))
            sys.exit(1)

results = []

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


