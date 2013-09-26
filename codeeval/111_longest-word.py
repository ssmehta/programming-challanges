#!/usr/bin/env python

"""
Longest Word

Challenge Description:

In this challenge you need to find the longest word in a sentence. If the sentence has more than one word of the same length you should pick the first one.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    some line with text
    another line

Each line has one or more words. Each word is separated by space char.

Output sample:

Print the longest word in the following way.

    some
    another
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            s = line.strip().split()
            lengths = list(map(len, s))
            
            print(s[lengths.index(max(lengths))])
