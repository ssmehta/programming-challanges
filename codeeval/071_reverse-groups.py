#!/usr/bin/env python

"""
Reverse Groups

Challenge Description:

Given a list of numbers and a positive integer k, reverse the elements of the list, k items at a time. If the number of elements is not a multiple of k, then the remaining items in the end should be left as is.

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a list of numbers and the number k, separated by a semicolon. The list of numbers are comma delimited. E.g.

    1,2,3,4,5;2
    1,2,3,4,5;3

Output sample:

Print out the new comma separated list of numbers obtained after reversing. E.g.

    2,1,4,3,5
    3,2,1,4,5
"""

from __future__ import print_function
import sys


if __name__ == '__main__':
    intcsv = lambda x: [int(s) for s in x.split(',')]
    
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                n, k = [f(x) for f, x in zip((intcsv, int), line.split(';'))]
                
                for i in range(0, len(n) - len(n) % k, k):
                    n[i : i + k] = reversed(n[i : i + k])
                
                print(*n, sep = ',')
