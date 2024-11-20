#!/usr/bin/env python3

import sys
#import re

with open(sys.argv[1], mode='r') as input:
    #t = input.read().strip().split("\n")
    diagram = input.read().strip()
diagram = diagram.replace('AND', '&')
diagram = diagram.replace('OR', '|')
diagram = diagram.replace('RSHIFT', '>>')
diagram = diagram.replace('LSHIFT', '<<')
diagram = diagram.replace('NOT', '~')
diagram = diagram.replace('is', 'iss')
diagram = diagram.replace('in', 'inn')
diagram = diagram.replace('as', 'ass')
diagram = diagram.replace('if', 'iff')

diagram = diagram.split("\n")

while True:
    try:
        a
        break
    except:
        for line in diagram:
            print(line)
            (args, result) = line.split(" -> ")
            try:    exec(f"{result} = {args}")
            except NameError: pass
            except SyntaxError:
                print("syntax error")
            except:
                print("unknown exception")
                print(line)
            
print(a)
