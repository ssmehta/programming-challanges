#!/usr/bin/env python

"""
First Non-Repeated Character

Challenge Description:

Write a program to find the first non repeated character in a string.

Input sample:

The first argument will be a text file containing strings. e.g. 

    yellow
    tooth

Output sample:

Print to stdout, the first non repeating character, one per line.
e.g.

    y
    h
"""

import collections, sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            
            if line:
                c = collections.Counter(line)
                
                for x in line:
                    if c[x] == 1:
                        print(x)
                        break
