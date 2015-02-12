#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        a, b, x = list(map(int, sys.stdin.readline().split()))
        
        n = a**b
        d = int(n / x)
        
        if abs(n - d * x) <= abs(n - (d + 1) * x):
            print(d * x)
        else:
            print((d + 1) * x)