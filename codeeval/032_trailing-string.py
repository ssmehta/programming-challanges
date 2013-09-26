#!/usr/bin/env python

"""
Trailing String

Challenge Description:

You are given two strings 'A' and 'B'. Print out a 1 if string 'B' occurs at the end of string 'A'. Else a zero.

Input sample:

The first argument is a file, containing two strings, comma delimited, one per line. Ignore all empty lines in the input file.e.g. 

    Hello World,World
    Hello CodeEval,CodeEval
    San Francisco,San Jose

Output sample:

Print out 1 if the second string occurs at the end of the first string. Else zero. Do NOT print out empty lines between your output. 
e.g.

    1
    1
    0x
"""

import math, sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            A, B = line.strip().split(',')
            print(int(A.endswith(B)))
