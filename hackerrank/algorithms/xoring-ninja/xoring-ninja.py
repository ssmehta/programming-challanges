#!/usr/bin/env python

import functools, operator as op, sys


MOD = 1000000007


bitfield = lambda n: [1 if d == '1' else 0 for d in bin(n)[2:][::-1]]


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        X = list(map(int, sys.stdin.readline().split()))

        x = functools.reduce(op.or_, X, 0)
        k = pow(2, N - 1, MOD)
        
        print(sum(k * (1 << i) for i, d in enumerate(bitfield(x)) if d) % MOD)