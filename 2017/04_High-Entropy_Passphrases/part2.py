#!/usr/bin/env python3

import sys
from itertools import permutations

t = []
linepassed = 0
counter = 0

def unique(list1):
    # put list to a set
    list_set = set(list1)
    # convert the set back to the list
    unique_list = (list(list_set))
    return unique_list

with open('input', mode='r') as input:
    for line in input:
        t = list(line.strip().split(' '))
        #print(line)
        passes = {}
        breakflag=False
        linepassed = True

        for pas in t:
            if not pas in passes:
                passes[pas] = 1
            else:
                linepassed = False
                break
        if linepassed:
          passes = {}
          for pas in t:
            perms = permutations(list(pas))
            for perm in unique(list(perms)):
                word = "".join(perm)
                if not word in passes:
                    passes[word] = 1
                else:
                    linepassed = False
                    #print("same word="+word)
                    breakflag = True
                    break
            if breakflag:
                break
        counter += linepassed

print("result = " + str(counter))
sys.exit(0)

