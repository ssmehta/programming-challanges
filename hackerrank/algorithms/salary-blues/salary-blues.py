#!/usr/bin/env python

import fractions as f, sys


if __name__ == '__main__':
    N, Q = list(map(int, sys.stdin.readline().split()))
    A = sorted(map(int, sys.stdin.readline().split()))
    
    
    if N == 1:
        # Process queries
        for _ in range(Q):
            K = int(sys.stdin.readline())
            print(A[0] + K)
        
    else:
        # Compute common gcd for A[1:]
        x = A[1] - A[0]
        
        for i in range(1, N):
            A[i] -= A[0]
            x = f.gcd(x, A[i])
        
        # Process queries
        for _ in range(Q):
            K = int(sys.stdin.readline())
            print(f.gcd(x, A[0] + K))