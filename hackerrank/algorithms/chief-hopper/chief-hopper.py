#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    H = list(map(int, sys.stdin.readline().split()))

    energy = 0

    for i in reversed(range(N)):
        energy = (energy + H[i] + 1) // 2

    print(energy)