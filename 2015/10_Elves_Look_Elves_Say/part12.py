#!/usr/bin/env python3

li = [1,3,2,1,1,3,1,1,1,2]
it = 0
le = []
tmp = []

while it < 50:
    for c in li:
        if len(tmp) == 0 or tmp[-1] == c:
            tmp.append(c)
        else:
            le.extend([len(tmp), tmp[0]])
            tmp = [c]
    le.extend([len(tmp), tmp[0]])
    li = le[::]
    tmp = []
    le = []
    it += 1
    print("%i  %i" % (it, len(li)))

