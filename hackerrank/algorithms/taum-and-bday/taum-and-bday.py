#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        B, W = list(map(int, sys.stdin.readline().split()))
        X, Y, Z = list(map(int, sys.stdin.readline().split()))

        if X + Z < Y:
            print(B * X + W * (X + Z))
        elif Y + Z < X:
            print(B * (Y + Z) + W * Y)
        else:
            print(B * X + W * Y)