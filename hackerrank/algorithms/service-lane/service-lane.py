#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N, T = list(map(int, sys.stdin.readline().split()))
    width = list(map(int, sys.stdin.readline().split()))
    
    for _ in range(T):
        i, j = list(map(int, sys.stdin.readline().split()))
        print(min(width[i : j + 1]))