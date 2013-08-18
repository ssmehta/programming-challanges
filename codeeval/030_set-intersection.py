#!/usr/bin/env python

"""
Set Intersection

Challenge Description:

You are given two sorted list of numbers (ascending order). The lists themselves are comma delimited and the two lists are semicolon delimited. Print out the intersection of these two sets.

Input sample:

File containing two lists of ascending order sorted integers, comma delimited, one per line. E.g. 

    1,2,3,4;4,5,6
    20,21,22;45,46,47
    7,8,9;8,9,10,11,12

Output sample:

Print out the ascending order sorted intersection of the two lists, one per line. Print empty new line in case the lists have no intersection. E.g. 

    4

    8,9
"""

import os, sys

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            a, b = [set(map(int, x.split(','))) for x in line.split(';')]
            print(','.join(map(str, sorted(a.intersection(b)))))
