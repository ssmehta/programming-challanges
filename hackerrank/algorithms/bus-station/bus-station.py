#!/usr/bin/env python

import itertools, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    S = sum(A)
    X = set(itertools.accumulate(A))

    for x in sorted(X):
        if S % x == 0:
            for i in range(1, S // x + 1):
                if (i * x) not in X:
                    break
            else:
                print(x, end = ' ' if x < S else '\n')