#!/usr/bin/env python

import math, sys


MOD = 1000000007


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, M = list(map(int, sys.stdin.readline().split()))
        print(math.factorial(N + M - 1) // math.factorial(N) // math.factorial(M - 1) % MOD)