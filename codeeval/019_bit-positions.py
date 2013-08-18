#!/usr/bin/env python

"""
Bit Positions

Challenge Description:

Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not. Positions p1 and p2 and 1 based.

Input sample:

The first argument will be a text file containing a comma separated list of 3 integers, one list per line. E.g.

    86,2,3
    125,1,2

Output sample:

Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase). E.g.

    true
    false
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            n, p1, p2 = list(map(int, line.split(',')))
            bits = bin(n)[2:]
            
            if p1 > len(bits) or p2 > len(bits):
                bits = '0' * (max(p1, p2) - len(bits)) + bits
            
            print('true' if bits[-p1] == bits[-p2] else 'false')
