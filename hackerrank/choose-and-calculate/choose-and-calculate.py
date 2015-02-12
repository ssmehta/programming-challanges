#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().split()))
    X = sorted(map(int, sys.stdin.readline().split()))
    
    choose = 1
    total = 0
    
    for i in range(N - K + 1):
        total += choose * (X[K + i - 1] - X[N - K - i]) % MOD
        choose = choose * (K + i) * pow(i + 1, MOD - 2, MOD) % MOD
    
    print(total % MOD)