#!/usr/bin/env python

import fractions, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        l, b = list(map(int, sys.stdin.readline().split()))
        print(l * b // fractions.gcd(l, b)**2)