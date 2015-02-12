#!/usr/bin/env python

import collections, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = sorted(map(int, sys.stdin.readline().split()))
        
        print(sum(v * (v - 1) for v in collections.Counter(A).values()))