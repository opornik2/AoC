#!/usr/bin/python3

import sys
import re
import time

debug = False
acum = 0
index = 1
cnt = dict()
changedjmp = 0
changed = 0
curjmp = 0

def acc(val):
    global acum
    acum += val

with open(sys.argv[1], mode='r') as inputfile:
    code = inputfile.read().strip().split('\n')

t = code[:]
while True:
    line = t[index-1]
    if index in cnt:
        cnt[index] += 1
    else:
        cnt[index] = 1
    if cnt[index] > 1:
        print("loop detected, acum=" + str(acum) + "\n\n\n")
        t = code[:]
        changed = 0
        index = 1
        cnt = {}
        acum = 0
        curjmp = 0
        print(str(changedjmp) + " jmp changed to nop\n")
        time.sleep(1)

    print(str(index) + ". " + line + "\tacum: " + str(acum))
    match = re.search(r'^(\w+) (.*)', line)
    if match.group(1) == 'acc':
        acc(int(match.group(2)))
        index += 1
    elif match.group(1) == 'jmp':
        curjmp += 1
        if changed == 0  and curjmp > changedjmp:
            #nop
            index +=1
            changedjmp = curjmp
            changed = 1
            print(str(changedjmp) + " jmp changed to nop @ " + str(index) + "\n\n")
        else:
            index += int(match.group(2))

    elif match.group(1) == 'nop':
        index += 1

