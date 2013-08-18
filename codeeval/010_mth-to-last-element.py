#!/usr/bin/env python

"""
Mth to last element

Challenge Description:

Write a program to determine the Mth to last element of a list. 
Input sample:

The first argument will be a text file containing a series of space delimited characters followed by an integer representing a index into the list (1 based), one per line. E.g. 

    a b c d 4
    e f g h 2

Output sample:

Print to stdout, the Mth element from the end of the list, one per line. If the index is larger than the list size, ignore that input. E.g.

    a
    g
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            elements = line.strip().split()
            idx = int(elements.pop())
            
            if idx <= len(elements):
                print(elements[-idx])
