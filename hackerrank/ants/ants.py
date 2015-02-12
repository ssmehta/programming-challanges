#!/usr/bin/env python

import sys


TIME = 1000000006
LENGTH = 1000
STEPS = 10


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    V = sorted(map(int, sys.stdin.readline().split()))

    x = 4 * TIME * (N // 2) * ((N % 2) + (N // 2)) // (LENGTH * STEPS)
    i = 0

    while i < N:
        if V[i] == (V[i - 1] + 1) % LENGTH:
            x += 2
            i += 1
        i += 1

    print(x)