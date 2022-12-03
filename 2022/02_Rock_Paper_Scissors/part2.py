#!/usr/bin/env python3

import sys
#Rock  A 1
#Paper B 2
#Sciss C 3
#X lose 0
#Y draw 3
#Z win  6

with open('input', mode='r') as input:
    t = input.read().strip().split('\n')

score = 0
for e in t:
    
    if e=="A X": score += 3
    elif e=="A Y": score += 4
    elif e=="A Z": score += 8
    elif e=="B X": score += 1
    elif e=="B Y": score += 5
    elif e=="B Z": score += 9
    elif e=="C X": score += 2
    elif e=="C Y": score += 6
    elif e=="C Z": score += 7

print(str(score))


