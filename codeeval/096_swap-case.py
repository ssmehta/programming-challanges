#!/usr/bin/env python

"""
Swap Case

Challenge Description:

Write a program which swaps letters' case in a sentence. All non-letter characters should remain the same.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    Hello world!
    JavaScript language 1.8
    A letter

Output sample:

Print results in the following way.

    hELLO WORLD!
    jAVAsCRIPT LANGUAGE 1.8
    a LETTER
"""

from __future__ import print_function
import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            for c in line:
                print(c.upper() if c.islower() else c.lower(), end = '')
