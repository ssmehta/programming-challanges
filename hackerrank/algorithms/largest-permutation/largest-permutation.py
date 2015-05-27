#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().split()))
    A = list(map(int, sys.stdin.readline().split()))
    
    if K >= N - 1:
        print(*sorted(A, reverse = True), sep = ' ')
    
    else:
        X = sorted(A)
        i, swaps = 0, 0
        
        while swaps < K:
            x = X.pop()
            
            if A[i] != x:
                A[A.index(x)] = A[i]
                A[i] = x
                swaps += 1
            
            i += 1
        
        print(*A, sep = ' ')