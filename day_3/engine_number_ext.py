#!/usr/bin/env python3
import re
import pprint
from collections import defaultdict

def isSymbolAdjacent(coord, gears):
    if (coord[0] - 1, coord[1] - 1) in gears:
        return (coord[0] - 1, coord[1] - 1)
    if (coord[0] - 1, coord[1]) in gears:
        return (coord[0] - 1, coord[1])
    if (coord[0] - 1, coord[1] + 1) in gears:
        return (coord[0] - 1, coord[1] + 1)
    if (coord[0], coord[1] - 1) in gears:
        return (coord[0], coord[1] - 1)
    if (coord[0], coord[1] + 1) in gears:
        return (coord[0], coord[1] + 1)
    if (coord[0] + 1, coord[1] - 1) in gears:
        return (coord[0] + 1, coord[1] - 1)
    if (coord[0] + 1, coord[1]) in gears:
        return (coord[0] + 1, coord[1])
    if (coord[0] + 1, coord[1] + 1) in gears:
        return (coord[0] + 1, coord[1] + 1)
    return False

def main():
    gears = set()
    with open('input.txt', 'r') as file:
        for (i, l) in enumerate(file):
            for (j, c) in enumerate(l):
                if m := re.match('\*', c):
                    gears.add((i, j))

    gear_parts, skip = defaultdict(list), 0
    with open('input.txt', 'r') as file:
        for (i, l) in enumerate(file):
            for (j, c) in enumerate(l):
                # Skips the next 'skip' digits such to not double count numbers (i.e. '567' + '67' + '7')
                if skip > 0:
                    skip -= 1
                    continue
                
                # Gathers all contiguous digits into a number.
                num, k = '', 0
                while m := re.match('\d', l[j + k]):
                    num += m.group(0)
                    k += 1
                
                # Determines if the number is adjacent to a symbol.
                for n in range(k):
                    if gear := isSymbolAdjacent((i, j + n), gears):
                        gear_parts[gear].append(num)
                        break
    
                skip = k
    
    # Calculates the gear ratio
    gear_ratio = 0
    for v in gear_parts.values():
      if len(v) != 2:
        continue
      
      gear_ratio += int(v[0]) * int(v[1])
      
    print(gear_ratio)         
                    
if __name__ == "__main__":
    main()