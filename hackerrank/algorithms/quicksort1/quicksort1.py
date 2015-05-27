#!/usr/bin/env python

import sys


def partition(ar):
    return [n for n in ar if n < ar[0]] + [n for n in ar if n >= ar[0]]

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    print(' '.join(map(str, partition(ar))))
