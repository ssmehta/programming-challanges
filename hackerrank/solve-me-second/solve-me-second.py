#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        A, B = list(map(int, sys.stdin.readline().split()))
        print(A + B)