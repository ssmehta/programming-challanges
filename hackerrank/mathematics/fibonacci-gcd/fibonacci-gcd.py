#!/usr/bin/env python

import fractions, functools, sys


MOD = 1000000007
FIB_MATRIX = [[1, 1], [1, 0]]


def matrix_mult(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) % MOD for B_col in zip(*B)] for A_row in A]

def matrix_exp(A, N):
    M = [[1, 0], [0, 1]]
    
    if N == 0:
        return M
    elif N == 1:
        return A
    else:
        P = matrix_exp(A, N // 2)
        P = matrix_mult(P, P)
        
        if N % 2 == 1:
            P = matrix_mult(P, A)
        
        return P

def fibonacci(N):
    return matrix_exp(FIB_MATRIX, N)[1][0]


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = [int(sys.stdin.readline()) for _ in range(N)]
    
    gcd = functools.reduce(fractions.gcd, A)
    print(fibonacci(gcd))