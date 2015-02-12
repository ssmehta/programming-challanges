#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    min_a, min_b = 0, 0
    
    for _ in range(N):
        a, b = list(map(int, sys.stdin.readline().split()))
        min_a = min(min_a, a) if min_a > 0 else a
        min_b = min(min_b, b) if min_b > 0 else b
    
    print(min_a * min_b)