#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        S = sys.stdin.readline().strip()
        print(sum(S[i - 1] == S[i] for i in range(1, len(S))))