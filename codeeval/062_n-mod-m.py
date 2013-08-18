#!/usr/bin/env python

"""
Hex to Decimal

Challenge Description:

You will be given a hexadecimal (base 16) number. Convert it into decimal (base 10).

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a hex number. You may assume that the hex number does not have the leading 'Ox'. Also all alpha characters (a through f) in the input will be in lowercase. E.g.

    9f
    11

Output sample:

Print out the equivalent decimal number. E.g.

    159
    17
"""

import sys


if __name__ == '__main__':
    key = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    
    with open(sys.argv[1]) as f:
        for line in f:
            total, multiplier = 0, 1
            
            for x in reversed(line.strip()):
                if x in key:
                    total += key[x] * multiplier
                else:
                    total += int(x) * multiplier
                
                multiplier *= 16
            
            print(total)
