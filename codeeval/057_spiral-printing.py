#!/usr/bin/env python

"""
Spiral Printing

Challenge Description:

Write a program to print a 2D array (n x m) in spiral order (clockwise)

Input sample:

Your program should accept as its first argument a path to a filename. The input file contains several lines. Each line is one test case. Each line contains three items (semicolon delimited). The first is 'n'(rows), the second is 'm'(columns) and the third is a single space separated list of characters/numbers in row major order. E.g.

    3;3;1 2 3 4 5 6 7 8 9

Output sample:

Print out the matrix in clockwise fashion, one per line, space delimited. E.g.

    1 2 3 6 9 8 7 4 5
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                n, m, x = line.split(';')
                n, m, x = int(n), int(m), x.strip().split()
                matrix = [x[i : i + m] for i in range(0, len(x), m)]
                
                x1, x2, y1, y2 = 0, m, 0, n
                numbers = []
                
                while x1 < x2 and y1 < y2:
                    if y1 < y2:
                        numbers.extend(matrix[y1][x] for x in range(x1, x2))
                        y1 += 1
                    
                    if x1 < x2:
                        numbers.extend(matrix[y][x2 - 1] for y in range(y1, y2))
                        x2 -= 1
                    
                    if y1 < y2:
                        numbers.extend(matrix[y2 - 1][x] for x in reversed(range(x1, x2)))
                        y2 -= 1
                    
                    if x1 < x2:
                        numbers.extend(matrix[y][x1] for y in reversed(range(y1, y2)))
                        x1 += 1
                
                print(' '.join(map(str, numbers)))
