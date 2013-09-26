#!/usr/bin/env python

"""
Pass Triangle

Challenge Description:

By starting at the top of the triangle and moving to adjacent numbers on the row below, the maximum total from top to bottom is 27.

       5
      9 6
     4 6 8
    0 7 1 5

5 + 9 + 6 + 7 = 27

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    5
    9 6
    4 6 8
    0 7 1 5

You make also check full [input file](http://www.yodlecareers.com/puzzles/triangle.txt) which will be used for your code evaluation.

Output sample:

The correct output is the maximum sum for the triangle. So for the given example the correct answer would be

    27
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        triangle = [list(map(int, line.split())) for line in f]
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
        
        print(max(triangle[-1]))
