#!/usr/bin/env python3

import sys
import re


with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

cards={}
summ=0
copy={}
for i in range (1,210): copy{i} = 1

for line in t:
    print(line)
    match = re.search('Card +(\d+): (.*)',line)
    game = int(match.group(1))
    cards{game} += 1
    winning = re.split(r' +', match.group(2).split("|")[0].strip())
    owned = re.split(r' +', match.group(2).split("|")[1].strip())
    points = 0
    for w in winning:
        if w in owned:
            points += 1
    for p in range(1, points+1):
        copy{game+p} += 1




print(summ)
