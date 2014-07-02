#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    
    total = 0
    
    for _ in range(M):
        a, b, k = list(map(int, sys.stdin.readline().split()))
        total += (b - a + 1) * k
    
    print(total // N)
