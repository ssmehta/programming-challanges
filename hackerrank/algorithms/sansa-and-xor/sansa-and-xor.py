#!/usr/bin/env python

import functools, operator as op, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
        
        print(functools.reduce(op.xor, (a for i, a in enumerate(A) if (i + 1) * (N - i) % 2 == 1), 0))