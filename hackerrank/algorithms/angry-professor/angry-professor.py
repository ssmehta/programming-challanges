#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, K = list(map(int, sys.stdin.readline().split()))
        X = list(map(int, sys.stdin.readline().split()))
        
        print('YES' if sum(1 for x in X if x <= 0) < K else 'NO')