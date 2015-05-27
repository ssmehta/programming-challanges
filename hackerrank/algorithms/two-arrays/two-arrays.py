#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, K = list(map(int, sys.stdin.readline().split()))
        A = sorted(map(int, sys.stdin.readline().split()))
        B = sorted(map(int, sys.stdin.readline().split()))
        
        for a, b in zip(A, reversed(B)):
            if a + b < K:
                print('NO')
                break
        else:
            print('YES')
