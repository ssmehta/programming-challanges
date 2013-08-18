#!/usr/bin/env python

"""
Fibonacci Series

Challenge Description:

The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n-1) + F(n-2) when n>1. Given a positive integer 'n', print out the F(n).

Input sample:

The first argument will be a text file containing a positive integer, one per line. E.g.

    5
    12

Output sample:

Print to stdout, the fibonacci number, F(n). E.g.

    5
    144
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            n = int(line)
            a, b, k = 0, 1, 0
            
            while k < n:
                a, b, k = b, a + b, k + 1
            
            print(a)
