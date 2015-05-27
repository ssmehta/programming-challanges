#!/usr/bin/env python

import fractions, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        a, b, x, y = list(map(int, sys.stdin.readline().split()))
        
        g1, g2 = fractions.gcd(a, b), fractions.gcd(x, y)
        print('YES' if x % g1 == 0 and y % g1 == 0 and a % g2 == 0 and b % g2 == 0 else 'NO')