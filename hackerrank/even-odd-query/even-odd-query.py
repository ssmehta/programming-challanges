#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    Q = int(sys.stdin.readline())
    
    for _ in range(Q):
        x, y = list(map(int, sys.stdin.readline().split()))
        
        if x == y or A[x] > 0:
            print('Even' if A[x - 1] % 2 == 0 else 'Odd')
        else:
            print('Odd')