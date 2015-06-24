#!/usr/env/bin python

import sys


MOD = 1000000007


def modinv(n, p):
    return pow(n, p - 2, p)

def mod_choose(n, k, m):
    if k < 0 or k > n:
        return 0
    
    else:
         p, q = 1, 1
         
         for i in range(1, min(k, n - k) + 1):
            p = (p * n) % m
            q = (q * i) % m
            n -= 1
         
         return (p * modinv(q, m)) % m


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        m, n = [int(x) for x in sys.stdin.readline().split()]
        print(mod_choose(n + m - 2, m - 1, MOD))