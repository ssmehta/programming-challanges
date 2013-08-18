#!/usr/bin/env python

"""
Simple Sorting

Challenge Description:

Write a program which sorts numbers.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    70.920 -38.797 14.354 99.323 90.374 7.581
    -37.507 -3.263 40.079 27.999 65.213 -55.552

Output sample:

Print sorted numbers in the following way.

    -38.797 7.581 14.354 70.920 90.374 99.323
    -55.552 -37.507 -3.263 27.999 40.079 65.213
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            numbers = sorted((float(s), s) for s in line.strip().split())
            print(' '.join(n[1] for n in numbers))
