#!/usr/bin/env python

"""
Even Numbers

Challenge Description:

Write a program which checks input numbers and determines whether a number is even or not.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    701
    4123
    2936

Output sample:

Print 1 if the number is even or 0 if the number is odd.

    0
    0
    1

All numbers in input are integers > 0 and < 5000.
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(int(int(line) % 2 == 0))
