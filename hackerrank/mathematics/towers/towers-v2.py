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
    DIM = max(A)
    M = [[int(i + 1 in A) for i in range(DIM)]]
    
    for i in range(1, DIM):
        x = [0] * DIM
        x[i - 1] = 1
        M.append(x)

    
    # Exponentiate matrix
    X = [[int(i == j) for j in range(DIM)] for i in range(DIM)]
    
    while N > 0:
        if N % 2 == 1:
            X = matrix_mult(X, M)
        M = matrix_mult(M, M)
        N //= 2
    
    print(2 * X[0][0] % MOD)