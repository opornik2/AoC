#!/usr/bin/python3

import sys
from math import floor
from itertools import permutations

phases = [0, 1, 2, 3, 4]

with open('input', mode='r') as input:
    t = input.read().split(",")
t = list(map(int, t))

#inputs = sys.argv
#inputs.pop(0)  #removes element 0
#inputs = list(map(int, inputs))

def intcomp(inp):
    global t
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
        #print("idx=%d, opcode=%d, 1mode=%d, 2mode=%d" % (cursor, opcode, mode[0], mode[1]))
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
            if output is None:
                t[t[cursor+1]] = inp.pop(0)
            else:
                t[t[cursor+1]] = output
                output = None
            cursor += 2

        elif opcode == 4: # output a
            output = t[t[cursor+1]]
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
            return output

        else:
            print("error! instruction at position %i = %i" % (cursor, (t[cursor])))
            sys.exit(1)

results = []

for ph in list(permutations(phases)):
    #print("phases:" + str(ph))
    result = 0 # second input to AmpA
    for amp in range(0,5):
        inputs = []
        inputs.append(ph[amp])  # first input to Amplifier
        inputs.append(result)   # second input as result from previous Amp
        result = intcomp(inputs)
    #print("output = %i\n" % (result))
    results.append(result)  # let's make a list of all results


print(max(results))


