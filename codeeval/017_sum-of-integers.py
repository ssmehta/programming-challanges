#!/usr/bin/env python

"""
Sum of integers

Challenge Description:

Write a program to determine the largest sum of contiguous integers in a list.

Input sample:

The first argument will be a text file containing a comma separated list of integers, one per line. e.g. 

    -10, 2, 3, -2, 0, 5, -15
    2,3,-2,-1,10

Output sample:

Print to stdout, the largest sum. In other words, of all the possible contiguous subarrays for a given array, find the one with the largest sum, and print that sum.
e.g.

    8
    12
"""

import math, sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            numbers = list(map(int, line.split(',')))
            
            max_sum, local_max = 0, 0
            
            for n in numbers:
                local_max = max(0, local_max + n)
                max_sum = max(max_sum, local_max)
            
            print(max_sum)
