#!/usr/bin/python3

import sys
import re

debug = False
acum = 0
index = 1
cnt = dict()

def acc(val):
    global acum
    acum += val

with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

while True:
    line = t[index-1]
    if index in cnt:
        cnt[index] += 1
    else:
        cnt[index] = 1
    if cnt[index] > 1:
        print("loop detected, acum=" + str(acum))
        break
    print(str(index) + ". " + line + "\tacum: " + str(acum))
    match = re.search(r'^(\w+) (.*)', line)
    if match.group(1) == 'acc':
        acc(int(match.group(2)))
        index += 1
    elif match.group(1) == 'jmp':
        index += int(match.group(2))
    elif match.group(1) == 'nop':
        index += 1

