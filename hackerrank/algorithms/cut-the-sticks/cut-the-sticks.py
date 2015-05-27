#!/usr/bin/env python

import collections, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = collections.Counter(map(int, sys.stdin.readline().split()))
    
    n = N
    
    for k in sorted(A):
        print(n)
        n -= A[k]