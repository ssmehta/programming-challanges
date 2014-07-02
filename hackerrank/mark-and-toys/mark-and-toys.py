#!/usr/bin/env python

import itertools, sys


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().split()))
    X = sorted(map(int, sys.stdin.readline().split()))
    
    print(max(i + 1 for i, x in enumerate(itertools.accumulate(X)) if x < K))
