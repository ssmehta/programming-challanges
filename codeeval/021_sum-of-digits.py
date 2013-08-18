#!/usr/bin/env python

"""
Sum of Digits

Challenge Description:

Given a positive integer, find the sum of its constituent digits.

Input sample:

The first argument will be a text file containing positive integers, one per line. E.g.

    23
    496

Output sample:

Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

    5
    19
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(sum(map(int, line.strip())))
