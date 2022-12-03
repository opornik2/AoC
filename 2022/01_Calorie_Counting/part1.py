#!/usr/bin/env python3

import sys

with open('input', mode='r') as input:
    t = input.read().strip().split('\n')

i = 0
elf = []
for e in t:
    if e=="":
        i += 1
        continue
    try: elf[i] += int(e)
    except: elf.append(int(e))

i = 0
max = 0
elf.sort()
for e in elf:
    print(str(e))


