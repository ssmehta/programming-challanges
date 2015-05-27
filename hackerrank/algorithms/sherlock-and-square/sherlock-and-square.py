#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        print((pow(2, N + 1, MOD) + 2) % MOD)