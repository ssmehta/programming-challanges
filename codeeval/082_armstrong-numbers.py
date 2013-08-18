#!/usr/bin/env python

"""
Armstrong Numbers

Challenge Description:

An Armstrong number is an n-digit number that is equal to the sum of the n'th powers of its digits. Determine if the input numbers are Armstrong numbers.

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file has a positive integer. E.g.

    6
    153
    351

Output sample:

Print out True/False if the number is an Armstrong number or not. E.g.

    True
    True
    False
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            n, s = int(line), line.strip()
            
            print(n == sum(k**len(s) for k in map(int, s)))
