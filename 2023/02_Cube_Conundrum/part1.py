#!/usr/bin/env python3

import sys
import re

#input_test="Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

max_r = 12
max_g = 13
max_b = 14

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

summ=0
for line in t:
    print(line)
    match = re.search('Game (\d+): (.*)',line)
    game = int(match.group(1))
    for group in match.group(2).split(";"):
        for color in group.split(","):
            sr = re.search('(\d+) red', color)
            sg = re.search('(\d+) green', color)
            sb = re.search('(\d+) blue', color)
            r = 0 if sr == None else int(sr.group(1))
            g = 0 if sg == None else int(sg.group(1))
            b = 0 if sb == None else int(sb.group(1))
            if r > max_r or g > max_g or b > max_b:
                print("impossible")
                game = 0
                break
    summ += game
print(summ)
