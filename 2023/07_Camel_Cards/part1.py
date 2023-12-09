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
    if max(val) == 5: hand_type.setdefault(6, []).append(hand) #poker
    elif max(val) == 4: hand_type.setdefault(5, []).append(hand) #4 same/kareta
    elif max(val) == 3: 
        if sorted(val, reverse=True)[1] < 2 : hand_type.setdefault(3, []).append(hand) #3 same
        else: hand_type.setdefault(4, []).append(hand) #full
    elif max(val) == 2: 
        if sorted(val, reverse=True)[1] == 2 : hand_type.setdefault(2, []).append(hand) #2 pairs
        else: hand_type.setdefault(1, []).append(hand) #1 pair
    else:
        hand_type.setdefault(0, []).append(hand)


with open(sys.argv[1], mode='r') as input:
    t = input.read().strip().split("\n")

for line in t:
    hand, bid = line.split()
    #T=a, J=b, Q=c, K=d, A=e
    table = str.maketrans('TJQKA', 'abcde')
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
