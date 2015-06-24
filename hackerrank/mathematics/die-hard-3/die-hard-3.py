#!/usr/bin/env python

import fractions, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        a, b, c = list(map(int, sys.stdin.readline().split()))
        print('YES' if c <= max(a, b) and c % fractions.gcd(a, b) == 0 else 'NO')