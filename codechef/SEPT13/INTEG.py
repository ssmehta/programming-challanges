#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = sorted(map(int, sys.stdin.readline().split()))
    X = int(sys.stdin.readline())
    
    # Remove completed elements
    while A[-1] >= 0:
        A.pop()
    
    print(-sum(A[:X]))
