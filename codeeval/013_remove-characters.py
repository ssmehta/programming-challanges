#!/usr/bin/env python

"""
Remove Characters

Challenge Description:

Write a program to remove specific characters from a string.

Input sample:

The first argument will be a text file containing an input string followed by a comma and then the characters that need to be scrubbed. e.g. 

    how are you, abc
    hello world, def

Output sample:

Print to stdout, the scrubbed strings, one per line. Trim out any leading/trailing whitespaces if they occur. 
e.g.

    how re you
    hllo worl
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            s, chars = line.split(',')
            print(s.translate(None, chars.strip()))
