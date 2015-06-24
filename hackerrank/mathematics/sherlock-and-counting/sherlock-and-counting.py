#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, K = list(map(int, sys.stdin.readline().split()))

        if N <= 4 * K:
            print(N - 1)
        else:
            discriminant = N * N - 4 * N * K
            minRoot = (N - discriminant**0.5) / 2
            maxRoot = (N + discriminant**0.5) / 2
            
            print(int(minRoot) + int(N - maxRoot))