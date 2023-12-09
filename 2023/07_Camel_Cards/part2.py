#!/usr/bin/env python3

import sys
import re
from collections import Counter

summ = 0
hand_count = {}
hand_type = {}
bids = {}
#types:
#6=poker, 5=4 same, 4=full, 3=3 same, 2=2 pairs, 1=pair, 0=high card

def count_hand(hand):
    #print sorted(set([i for i in mylist if mylist.count(i)>2]))
    hand_count[hand] = Counter(hand)

def find_type(hand):
    val = hand_count[hand].values()
    jokers = hand_count[hand].get('1', 0)
    
    if max(val) == 5:
        htype = 6
    elif max(val) == 4:
        htype = 5
    elif max(val) == 3:
        if sorted(val, reverse=True)[1] < 2:
            htype = 3
        else:
            htype = 4
    elif max(val) == 2:
        if sorted(val, reverse=True)[1] == 2:
            htype =2
        else:
            htype = 1
    else:
        htype = 0

    if jokers > 0:
        if htype == 0: htype = 1
        elif htype == 1:
            if jokers == 1: htype = 3
            elif jokers == 2: htype = 3
        elif htype == 2:
            if jokers == 1: htype = 4
            elif jokers == 2: htype = 5
        elif htype == 3:
            if jokers == 1: htype = 5
            elif jokers == 2: htype = 6
            elif jokers == 3: htype = 5
        elif htype == 4:
            htype = 6
        elif htype == 5:
            htype = 6
 
    hand_type.setdefault(htype, []).append(hand) #poker


with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

for line in t:
    hand, bid = line.split()
    #T=a, J=1, Q=c, K=d, A=e
    table = str.maketrans('TJQKA', 'a1cde')
    hand2 = hand.translate(table)
    bids[hand2] = int(bid)
    count_hand(hand2)
    find_type(hand2)

rank = 1
for i in range(0,7):
    if len(hand_type.get(i, [])) > 0:
        print(f"type {i}")
        for h in sorted(hand_type[i]):
            print(f"hand {h}    rank {rank}    bid {bids[h]}")
            summ += rank * bids[h]
            rank += 1

print(summ)
