#!/usr/bin/env python3
import sys

summ = 0
part = 2

with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

while t:
    line1 = t.pop(0)
    line2 = t.pop(0)
    line3 = t.pop(0)
    try: t.pop(0)
    except: pass
    x1 = int(line1.split(": ")[1].split(", ")[0].replace("X+", ""))
    y1 = int(line1.split(": ")[1].split(", ")[1].replace("Y+", ""))
    x2 = int(line2.split(": ")[1].split(", ")[0].replace("X+", ""))
    y2 = int(line2.split(": ")[1].split(", ")[1].replace("Y+", ""))
    x3 = int(line3.split(": ")[1].split(", ")[0].replace("X=", ""))
    y3 = int(line3.split(": ")[1].split(", ")[1].replace("Y=", ""))
    if part == 2:
        x3 += 10000000000000
        y3 += 10000000000000
    w = x1 * y2 - x2 * y1       # x3 = x1 + x2  w=x1*y2 - y1*x2   |x3 x2| wx=x3*y2-y2*x2  |x1 x3} wy=x1*y3-y1*x3
                                # y3 = y1 + y2                    |y3 y2|                 |y1 y3}
    wx = x3 * y2 - y3 * x2
    wy = x1 * y3 - y1 * x3
    
    x = wx / w
    y = wy / w
    if x != int(x) or y != int(y): continue
    print (f"{x}\t{y}\t{3*x+y}")
    summ += 3*x+y
print(summ)