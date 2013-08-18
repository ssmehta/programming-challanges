#!/usr/bin/env python

"""
Lowercase

Challenge Description:

Given a string write a program to convert it into lowercase.

Input sample:

The first argument will be a text file containing sentences, one per line. You can assume all characters are from the english language. E.g.

    HELLO CODEEVAL
    This is some text

Output sample:

Print to stdout, the lowercase version of the sentence, each on a new line. E.g.

    b
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(line.lower())
