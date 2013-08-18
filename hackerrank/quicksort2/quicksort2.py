#!/usr/bin/env python

import sys


def print_list(ar):
    print(' '.join(map(str, ar)))

def quicksort(ar):
    if len(ar) <= 1:
        return ar
    else:
        left = quicksort([n for n in ar if n < ar[0]])
        right = quicksort([n for n in ar if n > ar[0]])
        
        print_list(left + [ar[0]] + right)
        return left + [ar[0]] + right

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    quicksort(ar)
