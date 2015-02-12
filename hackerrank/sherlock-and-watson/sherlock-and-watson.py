#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N, K, Q = list(map(int, sys.stdin.readline().split()))
    A = list(map(int, sys.stdin.readline().split()))
    
    for _ in range(Q):
        x = int(sys.stdin.readline())
        print(A[(x - K) % N])