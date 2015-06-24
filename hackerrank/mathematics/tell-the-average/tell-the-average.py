#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))
    
    for i in range(1, N):
        L[0] = (L[0] + L[i] + L[0] * L[i]) % MOD

    print(L[0])