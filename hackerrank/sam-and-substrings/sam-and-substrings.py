#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    N = list(map(int, list(sys.stdin.readline().strip())))

    total = 0
    k = 1

    for i, digit in enumerate(reversed(N)):
        total += k * digit * (len(N) - i) % MOD
        k = ((10 * k) + 1) % MOD

    print(total % MOD)