#!/usr/bin/env python

"""
Calculate Distance

Challenge Description:

You have coordinates of 2 points and need to find the distance between them.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    (25, 4) (1, -6)
    (47, 43) (-25, -11)

All numbers in input are integers between -100 and 100.

Output sample:

Print results in the following way.

    26
    90

You don't need to round the results you receive. 
They must be integer numbers between -100 and 100.
"""

import re, sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            m = list(map(int, re.findall(r'(-?\d+)', line)))
            print(int((abs(m[0] - m[2])**2 + abs(m[1] - m[3])**2)**0.5))
