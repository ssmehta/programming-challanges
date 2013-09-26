#!/usr/bin/env python

"""
Pascals Triangle

Challenge Description:

A Pascals triangle row is constructed by looking at the previous row and adding the numbers to its left and right to arrive at the new value. If either the number to its left/right is not present, substitute a zero in it's place. More details can be found here: http://en.wikipedia.org/wiki/Pascal's_triangle. E.g. a Pascals triangle upto a depth of 6 can be shown as:

                1
              1   1
            1   2   1
           1  3   3   1
         1  4   6   4   1
        1  5  10  10  5   1

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer which indicates the depth of the triangle (1 based). E.g.

    6

Output sample:

Print out the resulting pascal triangle upto the requested depth in row major form. E.g.

    1 1 1 1 2 1 1 3 3 1 1 4 6 4 1 1 5 10 10 5 1
"""

from __future__ import print_function
import sys


if __name__ == '__main__':
    triangle = [1]
    depth = 1
    
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                n = int(line)
                
                while n > depth:
                    last = triangle[-depth:]
                    triangle.extend([sum(last[max(0, i - 1) : i + 1]) for i in range(depth + 1)])
                    depth += 1
                
                print(*triangle[: n * (n + 1) // 2], sep = ' ')
