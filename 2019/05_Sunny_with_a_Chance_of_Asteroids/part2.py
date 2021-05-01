#!/bin/env python

import sys
# opcode modes: 0=position mode (index), 1=immediate mode (value)

with open('input', mode='r') as input:
	t = input.read().split(",")
t = list(map(int, t))
io = 5

cursor = 0
while(1):
	opcode = t[cursor] % 100
	mode = []
	mode = map(int, str(t[cursor] / 100))
	mode.reverse()
	for i in range(0,2):
		try: mode[i]
		except: mode.append(0)
	print("idx=%d, opcode=%d, 1mode=%d, 2mode=%d" % (cursor, opcode, mode[0], mode[1]))
	try:
		p1 = t[cursor+1] if mode[0] == 1 else t[t[cursor+1]]
		p2 = t[cursor+2] if mode[1] == 1 else t[t[cursor+2]]
	except: pass

	if opcode == 1:
		t[t[cursor+3]] = p1 + p2
		cursor += 4

	elif opcode == 2:
		t[t[cursor+3]] = p1 * p2
		cursor += 4
	
	elif opcode == 3:
		t[t[cursor+1]] = io
		cursor += 2
	
	elif opcode == 4:
		io = t[t[cursor+1]]
		print("output=%i" % (io))
		cursor += 2
	
	elif opcode == 5:
		if p1 != 0: cursor = p2
		else: cursor += 3

	elif opcode == 6:
		if p1 == 0: cursor = p2
		else: cursor += 3

	elif opcode == 7:
		if p1 < p2: t[t[cursor+3]] = 1
		else: t[t[cursor+3]] = 0
		cursor += 4

	elif opcode == 8:
		if p1 == p2: t[t[cursor+3]] = 1
		else: t[t[cursor+3]] = 0
		cursor += 4

	elif opcode == 99:
		print "HALT, result = " + str(io)
		sys.exit(0)
	
	else:
		print "error! instruction at position " + str(cursor) + " = " + str(t[cursor])
		sys.exit(1)

