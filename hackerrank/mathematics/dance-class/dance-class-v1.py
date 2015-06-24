#!/usr/bin/env python

import sys


def isqrt(n):
    """http://stackoverflow.com/a/15391420/406772"""

    x = n
    y = (n + 1) // 2
    
    while y < x:
        x = y
        y = (x + n // x) // 2
    
    return x


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        print('even' if isqrt(N) % 2 == 0 else 'odd')