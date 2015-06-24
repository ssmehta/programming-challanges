#!/usr/bin/env python

import sys


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


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        A, B, N = list(map(int, sys.stdin.readline().split()))

        M = matrix_exp(FIB_MATRIX, N)
        print((M[1][0] * B + M[1][1] * A) % MOD)