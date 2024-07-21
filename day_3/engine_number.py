#!/usr/bin/env python3
import re

def isSymbolAdjacent(coord, symbols):
    if (coord[0] - 1, coord[1] - 1) in symbols:
        return True
    if (coord[0] - 1, coord[1]) in symbols:
        return True
    if (coord[0] - 1, coord[1] + 1) in symbols:
        return True
    if (coord[0], coord[1] - 1) in symbols:
        return True
    if (coord[0], coord[1] + 1) in symbols:
        return True
    if (coord[0] + 1, coord[1] - 1) in symbols:
        return True
    if (coord[0] + 1, coord[1]) in symbols:
        return True
    if (coord[0] + 1, coord[1] + 1) in symbols:
        return True
    return False

def main():
    symbols = set()
    with open('input.txt', 'r') as file:
        for (i, l) in enumerate(file):
            for (j, c) in enumerate(l):
                if m := re.match('[^\d.\n]', c):
                    symbols.add((i, j))

    tot, skip = 0, 0
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
                    if isSymbolAdjacent((i, j + n), symbols):
                        tot += int(num)
                        break
    
                skip = k
    print(tot)          
                    
if __name__ == "__main__":
    main()