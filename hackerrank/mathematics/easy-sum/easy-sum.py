#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    triangular_number = lambda n: n * (n + 1) // 2
    
    for _ in range(T):
        N, m = list(map(int, sys.stdin.readline().split()))
        print((N // m) * triangular_number(m - 1) + triangular_number(N % m))