#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        A, B = list(map(int, sys.stdin.readline().split()))
        print(pow(A, B, MOD))
