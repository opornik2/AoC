#!/usr/bin/python3

import sys
from math import floor

# opcode modes: 0=position mode (index), 1=immediate mode (value)

with open('input', mode='r') as input:
    t = input.read().split(",")
t = list(map(int, t))

input_a = int(sys.argv[1])

def intcomp(inputa):
    global t
    cursor = 0
    while(1):
        opcode = t[cursor] % 100
        mode = []
        mode = list(map(int, str(floor(t[cursor] / 100))))
        mode.reverse()
        for i in range(0,2):
            try: mode[i]
            except: mode.append(0)
        print("idx=%d, opcode=%d, 1mode=%d, 2mode=%d" % (cursor, opcode, mode[0], mode[1]))
        try:
            p1 = t[cursor+1] if mode[0] == 1 else t[t[cursor+1]]
            p2 = t[cursor+2] if mode[1] == 1 else t[t[cursor+2]]
        except: pass

        if opcode == 1: # add a+b
            t[t[cursor+3]] = p1 + p2
            cursor += 4

        elif opcode == 2: # multiply a*b
            t[t[cursor+3]] = p1 * p2
            cursor += 4

        elif opcode == 3: # store input to a
            t[t[cursor+1]] = inputa
            cursor += 2

        elif opcode == 4: # output a
            output_a = t[t[cursor+1]]
            #print("output=%i" % (output_a))
            cursor += 2

        elif opcode == 5: # if a<>0 jump to b
            if p1 != 0: cursor = p2
            else: cursor += 3

        elif opcode == 6: # if a==0 jump to b
            if p1 == 0: cursor = p2
            else: cursor += 3

        elif opcode == 7: # if a<b c=1, else c=0
            if p1 < p2: t[t[cursor+3]] = 1
            else: t[t[cursor+3]] = 0
            cursor += 4

        elif opcode == 8: # if a==b c=1, else c=0
            if p1 == p2: t[t[cursor+3]] = 1
            else: t[t[cursor+3]] = 0
            cursor += 4

        elif opcode == 99: # HALT
            #print("HALT")
            return output_a

        else:
            print("error! instruction at position %i = %i" % (cursor, (t[cursor])))
            sys.exit(1)

result = intcomp(input_a)
print("output = %i" % (result))

