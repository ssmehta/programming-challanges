#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    X = sorted(int(sys.stdin.readline()) for _ in range(N))
    
    print(min(X[i + K - 1] - X[i] for i in range(0, N - K - 1)))
