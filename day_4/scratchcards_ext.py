#!/usr/bin/env python3
import re
import pprint
from collections import defaultdict

card_matches = dict()
card_counts = defaultdict(lambda: 1)

with open('input.txt', 'r') as cards:
  for card in cards:    
    if m := re.search(r'Card +(\d+):([\d ]+)\|([\d ]+)', card):
      card_no = m.group(1)
      winning_nums = set(filter(lambda v: v != '', m.group(2).split(' ')))
      scratch_nums = set(filter(lambda v: v != '', m.group(3).split(' ')))
      
      card_matches[int(card_no)] = len(winning_nums & scratch_nums)

with open('input.txt', 'r') as cards:
  for (card_no, card) in enumerate(cards, start=1):
    for i in range(card_counts[card_no]):
      for j in range(card_matches[card_no]):
        card_counts[card_no + 1 + j] += 1

print(sum(card_counts.values()))