#!/usr/bin/env python

import itertools, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    X = sorted(int(sys.stdin.readline()) for _ in range(N))
    
    S = list(itertools.accumulate(X))
    
    min_unfairness = unfairness = sum(i * X[i] - S[i - 1] for i in range(1, K))
    
    for i in range(1, N - K + 1):
        unfairness += (K - 1) * (X[i + K - 1] + X[i - 1])
        unfairness -= 2 * (S[i + K - 2] - S[i - 1])
        min_unfairness = min(min_unfairness, unfairness)
    
    print(min_unfairness)
