#!/bin/env python

import sys

with open('input', mode='r') as input:
	t = input.read().split(",")
t = list(map(int, t))
o = t[:]

for a in range(0,100):
	for b in range (0,100):
		t[1] = a
		t[2] = b
		cursor = 0
		while(1):
			if t[cursor] == 1:
				t[t[cursor+3]] = t[t[cursor+1]] + t[t[cursor+2]]
				cursor += 4
				continue
			elif t[cursor] == 2:
				t[t[cursor+3]] = t[t[cursor+1]] * t[t[cursor+2]]
				cursor += 4
				continue
			elif t[cursor] == 99:
				print "HALT, result = " + str(t[0]) + ", a = "+str(a)+", b = "+str(b)
				if t[0] == 19690720:
					print "found the right pair: a = "+str(a)+", b = "+str(b)
					sys.exit(0)
				else:
					t = o[:]
					break
			else:
				print "error! instruction at position " + str(cursor) + " = " + str(t[cursor])
				sys.exit(1)

