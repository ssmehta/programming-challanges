#!/usr/bin/env python

"""
Stack Implementation

Challenge Description:

Write a program implementing a stack inteface for integers.The interface should have 'push' and 'pop' functions. You will be asked to 'push' a series of integers and then 'pop' and print out every alternate integer.

Input sample:

The first argument will be a text file containing a series of space delimited integers, one per line. e.g. 

    1 2 3 4
    10 -2 3 4

Output sample:

Print to stdout, every alternate integer(space delimited), one per line.
e.g.

    4 2
    4 -2
"""

from __future__ import print_function
import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                stack = list(map(int, line.split()))
                
                for i in range(len(stack)):
                    x = stack.pop()
                    
                    if i % 2 == 0:
                        print(x, end = ' ')
                print()
