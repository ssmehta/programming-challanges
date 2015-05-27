#!/usr/bin/env python

import itertools, sys


if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    x = [0] * N

    for _ in range(M):
        a, b, k = list(map(int, sys.stdin.readline().split()))

        x[a - 1] += k
        if b < N:
            x[b] -= k

    print(max(itertools.accumulate(x)))