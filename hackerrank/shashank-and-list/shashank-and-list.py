#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    
    P = 1
    
    for a in A:
        P = P * (1 + pow(2, a, MOD)) % MOD
    
    print((P - 1) % MOD)
