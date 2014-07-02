#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        print(pow(n, 2, MOD))