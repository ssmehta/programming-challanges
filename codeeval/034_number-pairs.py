#!/usr/bin/env python

"""
Number Pairs

Challenge Description:

You are given a sorted array of positive integers and a number 'X'. Print out all pairs of numbers whose sum is equal to X. Print out only unique pairs and the pairs should be in ascending order

Input sample:

Your program should accept as its first argument a filename. This file will contain a comma separated list of sorted numbers and then the sum 'X', separated by semicolon. Ignore all empty lines. If no pair exists, print the string NULL eg.

    1,2,3,4,6;5
    2,4,5,6,9,11,15;20
    1,2,3,4;50

Output sample:

Print out the pairs of numbers that equal to the sum X. The pairs should themselves be printed in sorted order i.e the first number of each pair should be in ascending order .e.g.

    1,4;2,3
    5,15;9,11
    NULL
"""

from __future__ import print_function
import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                numbers, X = line.split(';')
                numbers, X = list(map(int, numbers.split(','))), int(X)
                
                pairs = []
                
                for n in numbers:
                    if n <= X // 2:
                        if X - n in numbers and n != X - n:
                            pairs.append('%d,%d' % (n, X - n))
                    else:
                        break
                
                print(';'.join(pairs) if pairs else 'NULL')
