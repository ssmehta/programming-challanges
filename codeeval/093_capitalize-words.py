#!/usr/bin/env python

"""
Capitalize Words

Challenge Description:

Write a program which capitalizes words in a sentence.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    Hello world
    javaScript language
    a letter

Output sample:

Print capitalized words in the following way.

    Hello World
    JavaScript Language
    A Letter
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(' '.join(s[0].upper() + s[1:] for s in line.strip().split()))
