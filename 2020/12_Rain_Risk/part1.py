#!/usr/bin/python3

import sys

x = 0
y = 0
heading = 'e'
rrotations = {
    'e':{90:'s', 180:'w', 270:'n'},
    'w':{90:'n', 180:'e', 270:'s'},
    's':{90:'w', 180:'n', 270:'e'},
    'n':{90:'e', 180:'s', 270:'w'}
    }
lrotations = {
    'e':{90:'n', 180:'w', 270:'s'},
    'w':{90:'s', 180:'e', 270:'n'},
    's':{90:'e', 180:'n', 270:'w'},
    'n':{90:'w', 180:'s', 270:'e'}
    }



def move(a, b):
    global x
    global y
    global heading
    if   'E' in a: x += b
    elif 'W' in a: x -= b
    elif 'N' in a: y += b
    elif 'S' in a: y -= b
    elif 'F' in a:
        if   heading == 'e': x += b
        elif heading == 'w': x -= b
        elif heading == 'n': y += b
        elif heading == 's': y -= b
    return


with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

for el in t:
    print(el)
    a = el[0]
    b = int(el[1:])
    if   'R' in a: heading = rrotations[heading][b]
    elif 'L' in a: heading = lrotations[heading][b]
    else: move(a, b)
    print(f'I am at {x}, {y}, heading {heading}')

print('Manhattan distance is %i' % (abs(x)+abs(y)))
