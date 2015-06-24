#!/usr/bin/env python

import sys


if __name__ == '__main__':
    L, S1, S2 = list(map(int, sys.stdin.readline().split()))
    Q = int(sys.stdin.readline())

    for _ in range(Q):
        q = int(sys.stdin.readline())
        print('%.4f' % (2**0.5 * (L - q**0.5) / abs(S1 - S2)))