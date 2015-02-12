#!/usr/bin/env python3

"""
Mixed Content

Challenge Description:

You have a string of words and digits divided by comma. Write a program which separates words with digits. You shouldn't change the order elements.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21
    24,13,14,43,41

Output sample:

    melon,apricot,peach,pineapple|8,33,21,0,16,50,37,0,7,17,21
    24,13,14,43,41
"""

import itertools, sys


def partition(pred, iterable):
    'Use a predicate to partition entries into false entries and true entries'
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = itertools.tee(iterable)
    return list(itertools.filterfalse(pred, t1)), list(filter(pred, t2))


if __name__ == '__main__':
    is_int = lambda s: all(c.isdigit() for c in s)
    
    with open(sys.argv[1]) as f:
        for line in f:
            words, ints = partition(is_int, line.strip().split(','))
            
            if words:
                print(*words, sep = ',', end = '|' if ints else '\n')
            if ints:
                print(*ints, sep = ',')
