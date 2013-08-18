#!/usr/bin/env python

"""
Penultimate Word

Challenge Description:

Write a program which finds the next-to-last word in a string.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    some line with text
    another line

Each line has more than one word.

Output sample:

Print the next-to-last word in the following way.

    with
    another
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(line.split()[-2])
