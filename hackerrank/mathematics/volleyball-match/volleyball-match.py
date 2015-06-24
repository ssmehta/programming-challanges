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
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    A, B = max(A, B), min(A, B)
    
    if A == 25 and B < 24:
        print(choose(A + B - 1, B) % MOD)
    elif B >= 24 and A - B == 2:
        print(pow(2, A - 26, MOD) * choose(48, 24) % MOD)
    else:
        print(0)