#!/usr/bin/env python

import itertools, operator as op, sys


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().split()))
    S = list(map(int, sys.stdin.readline().strip()))
    
    A, B = [S[0]], [S[0]]
    
    for i in range(1, len(S) - K + 1):
        x = A[-1] ^ S[i]
        
        B.append(A[-K] ^ x if len(A) >= K else x)
        A.append(A[-1] ^ B[-1])
    
    print(''.join(map(str, B)))