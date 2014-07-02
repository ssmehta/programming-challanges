#!/usr/bin/env python

import collections, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = {}
    
    for a in map(int, sys.stdin.readline().split()):
        if a not in A:
            A[a] = 0
        A[a] += 1
    
    M = int(sys.stdin.readline())
    for b in map(int, sys.stdin.readline().split()):
        A[b] -= 1
    
    print(*sorted(k for k in A if A[k]))