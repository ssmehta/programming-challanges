#!/usr/bin/env python

"""
Sum of Integers from File

Challenge Description:

Print out the sum of integers read from a file.

Input sample:

The first argument to the program will be a text file containing a positive integer, one per line. E.g.

    5
    12

Output sample:

Print out the sum of all the integers read from the file. E.g.

    17
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        print(sum(int(line) for line in f))
