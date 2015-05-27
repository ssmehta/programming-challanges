#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))

        if N == 1:
            print('YES')
        elif N == 2:
            print('NO')
        else:
            L, R = 0, sum(A[1:])

            for i in range(1, N - 1):
                L, R = L + A[i - 1], R - A[i]

                if L == R:
                    print('YES')
                    break
            else:
                print('NO')
