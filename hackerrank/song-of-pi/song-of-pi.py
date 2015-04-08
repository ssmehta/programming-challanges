#!/usr/bin/env python

import sys


PI = "3.1415926535897932384626433833"
PI_DIGITS = list(map(int, (c for c in PI if c.isdigit())))


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        S = list(map(len, sys.stdin.readline().strip().split()))
        print("It's a pi song." if S == PI_DIGITS[: len(S)] else "It's not a pi song.")