#!/usr/bin/env python

"""
Unique Elements

Challenge Description:

You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.

Input sample:

File containing a list of sorted integers, comma delimited, one per line. E.g. 

    1,1,1,2,2,3,3,4,4
    2,3,4,5,5

Output sample:

Print out the sorted list with duplicates removed, one per line. E.g.

    1,2,3,4
    2,3,4,5
"""

import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            s = set(map(int, line.split(',')))
            print(','.join(map(str, sorted(s))))
