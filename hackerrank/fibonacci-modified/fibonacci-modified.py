#!/usr/bin/env python

import sys


if __name__ == '__main__':
    A, B, N = list(map(int, sys.stdin.readline().split()))
    
    for _ in range(N - 2):
        A, B = B, A + B * B
    
    print(B)