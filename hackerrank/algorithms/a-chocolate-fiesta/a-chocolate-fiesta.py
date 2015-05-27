#!/usr/bin/env python

import sys


MOD = 1000000007


def choose(n, k):
    if k < 0 or k > n:
        return 0
    
    else:
         p, q = 1, 1
         
         for i in range(1, min(k, n - k) + 1):
            p *= n
            q *= i
            n -= 1
         
         return p // q


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    
    odds = sum(a % 2 for a in A)
    evens = N - odds
    
    n_evens = pow(2, evens, MOD) - 1
    
    if odds == 0:
        print(n_evens)
    else:
        n_odds = pow(2, odds - 1, MOD) - 1
        print((n_evens * n_odds + n_evens + n_odds) % MOD)