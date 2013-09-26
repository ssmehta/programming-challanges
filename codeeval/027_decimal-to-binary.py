#!/usr/bin/env python

"""
Decimal To Binary

Challenge Description:

Given a decimal (base 10) number, print out its binary representation.

Input sample:

File containing positive whole decimal numbers, one per line. e.g. 

    2
    10
    67

Output sample:

Print the decimal representation, one per line.
e.g.

    10
    1010
    1000011
"""

import math, sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(bin(int(line))[2:])
