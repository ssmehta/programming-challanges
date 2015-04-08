#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        A, M = list(map(int, sys.stdin.readline().split()))
        
        if M == 2:
            print('YES')
        else:
            print('NO' if pow(A, (M - 1) // 2, M) == M - 1 else 'YES')