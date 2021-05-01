#!/bin/env python

import sys

with open('input', mode='r') as input:
	t = input.read().split(",")
t = list(map(int, t))
t[1] = 12
t[2] = 2

cursor = 0
while(1):
	if t[cursor] == 1:
		t[t[cursor+3]] = t[t[cursor+1]] + t[t[cursor+2]]
	elif t[cursor] == 2:
		t[t[cursor+3]] = t[t[cursor+1]] * t[t[cursor+2]]
	elif t[cursor] == 99:
		print "HALT, result = " + str(t[0])
		sys.exit(0)
	else:
		print "error! instruction at position " + str(cursor) + " = " + str(t[cursor])
		sys.exit(1)
	cursor += 4

