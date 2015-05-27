#!/usr/bin/env python

import fractions, functools, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
        
        gcd = functools.reduce(fractions.gcd, A)
        print('YES' if gcd == 1 else 'NO')