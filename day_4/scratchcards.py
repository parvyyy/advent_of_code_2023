#!/usr/bin/env python3
import re

tot = 0
with open('small_input.txt', 'r') as cards:
  for card in cards:
    card_matches = 0
    
    if m := re.search(r'([\d ]+)\|([\d ]+)', card):
      winning_nums = m.group(1).split(' ')
      winning_nums = set(filter(lambda v: v != '', winning_nums))
      
      scratch_nums = m.group(2).split(' ')
      scratch_nums = filter(lambda v: v != '', scratch_nums)
      
      for num in scratch_nums:
        if num in winning_nums:
          card_matches += 1
      
      if card_matches > 0:
        tot += (2 ** (card_matches - 1))
    
print(tot) #22674