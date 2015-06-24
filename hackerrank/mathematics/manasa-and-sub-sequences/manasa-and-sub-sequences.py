#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    N = list(map(int, list(sys.stdin.readline().strip())))

    total = 0
    k = 0

    for i, digit in enumerate(N):
        total += (10 * total + (k + 1) * digit) % MOD
        k = (2 * k + 1) % MOD

    print(total % MOD)