#!/usr/bin/env python

import functools, operator as op, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        int(sys.stdin.readline())
        N = [int(x) for x in sys.stdin.readline().split()]
        print(functools.reduce(op.mul, N, 1) % 1234567)
