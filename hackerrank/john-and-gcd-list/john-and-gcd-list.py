#!/usr/bin/env python

import fractions, sys


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    
    B = [A[0]]
