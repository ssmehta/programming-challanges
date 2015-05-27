#!/usr/bin/env python

import sys


if __name__ == '__main__':
    a, b = list(map(int, sys.stdin.readline().split()))
    
    x = 2
    
    for _ in range(a):
        x = pow(x, 2, b)
    
    print(x)