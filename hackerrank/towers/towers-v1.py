#!/usr/bin/env python

import sys


MOD = 1000000007
MAX = 15


def matrix_mult(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) % MOD for B_col in zip(*B)] for A_row in A]


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    
    
    # Build matrix
    n = max(A)
    M = [[int(i + 1 in A) for i in range(n)]]
    
    for i in range(1, n):
        x = [0] * n
        x[i - 1] = 1
        M.append(x)
    
    
    # Exponentiate matrix
    exp = {1: [x[:] for x in M]}
    k = 1
    
    while k < N:
        i = max(j for j in exp if j <= N - k)
        M = matrix_mult(M, exp[i])
        
        k += i
        exp[k] = [x[:] for x in M]
    
    print(2 * M[0][0] % MOD)