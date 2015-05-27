#!/usr/bin/env python

import functools, operator as op, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    
    print(functools.reduce(op.xor, A))
