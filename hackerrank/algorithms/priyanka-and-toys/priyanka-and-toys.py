#!/usr/bin/env python

import sys


K = 4


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    W = sorted(map(int, sys.stdin.readline().split()))

    chosen = [W[0]]

    for w in W:
        if w > chosen[-1] + K:
            chosen.append(w)

    print(len(chosen))