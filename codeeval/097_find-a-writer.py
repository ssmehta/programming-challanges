#!/usr/bin/env python

"""
Find a Writer

Challenge Description:

You have a set of rows with names of famous writers encoded inside. Each row is divided into 2 parts by pipe char (|). The first part has a writer's name. The second part is a "key" to generate a name.

Your goal is to go through each number in the key (numbers are separated by space) left-to-right. Each number represents a position in the 1st part of a row. This way you collect a writer's name which you have to output.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg| 3 35 27 62 51 27 46 57 26 10 46 63 57 45 15 43 53

    3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA| 2 26 33 55 34 50 33 61 44 28 46 32 28 30 3 50 34 61 40 7 1 31

This input had 2 rows.

Output sample:

Print results in the following way.

    Stephen King 1947
    Kyotaro Nishimura 1930
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            code, key = line.split('|')
            key = list(map(int, key.strip().split()))
            
            print(''.join(code[k - 1] for k in key))
