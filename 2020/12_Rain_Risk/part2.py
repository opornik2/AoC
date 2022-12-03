#!/usr/bin/python3

import sys

#obroty wzgledem 0,0
#L90=R270=  -y, x
#L180=R180= -x, -y
#L270=R90=  y, -x

#jesli wzgledem a,b, to przed obrotem odjac:
#x' = x-a
#y' = y-b
#a po oborcie dodac ponownie
#x=x'+a
#y=y'+b

#waypoint
wpx = 10
wpy = 1
#ship
shx = 0
shy = 0

heading = 'e'

def rotate(a):
    global wpx
    global wpy
    global shx
    global shy
    x = wpx - shx
    y = wpy - shy
    if a=='L90' or a=='R270':
        newx = -y
        newy = x
    elif a=='L180' or a=='R180':
        newx = -x
        newy = -y
    elif a=='R90' or a=='L270':
        newx = y
        newy = -x
    wpx = newx + shx
    wpy = newy + shy

def wp(a, b):
    global wpx
    global wpy
    if   'E' in a: wpx += b
    elif 'W' in a: wpx -= b
    elif 'N' in a: wpy += b
    elif 'S' in a: wpy -= b

def move(b):
    global wpx
    global wpy
    global shx
    global shy
    x = wpx - shx
    y = wpy - shy
    shx += b * x
    shy += b * y
    wpx = shx + x
    wpy = shy + y


with open(sys.argv[1], mode='r') as inputfile:
    t = inputfile.read().strip().split('\n')

for el in t:
    print(el)
    a = el[0]
    b = int(el[1:])
    if 'R' in a or 'L' in a:
        rotate(el)
    elif 'F' in a:
        move(b)
    else:
        wp(a, b)
    print(f'Ship @ {shx}, {shy},  waypoint @ {wpx}, {wpy}')

print('Manhattan distance is %i' % (abs(shx)+abs(shy)))

