#!/usr/bin/env python

"""
Reverse words

Challenge Description:

Write a program to reverse the words of an input sentence.

Input sample:

The first argument will be a text file containing multiple sentences, one per line. Possibly empty lines too. E.g.

    Hello World
    Hello CodeEval

Output sample:

Print to stdout, each line with its words reversed, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces on each line you print. E.g.

    World Hello
    CodeEval Hello
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line:
                print(' '.join(line.split()[::-1]))
