#!/usr/bin/env python

"""
Number of Ones

Challenge Description:

Write a program to determine the number of 1 bits in the internal representation of a given integer.

Input sample:

The first argument will be a text file containing an integer, one per line. e.g. 

    10
    22
    56

Output sample:

Print to stdout, the number of ones in the binary form of each number.
e.g.

    2
    3
    3
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(bin(int(line)).count('1'))
