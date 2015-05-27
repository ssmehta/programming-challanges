#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    X = sorted(int(sys.stdin.readline()) for _ in range(N))
    
    diff = [X[i + 1] - X[i] for i in range(N - 1)]
    
    # Mulitply difference terms by multiplication table read by antidiagonals
    unfairness = lambda diff: sum((i + 1) * (K - i - 1) * d for i, d in enumerate(diff))
    
    print(min(unfairness(diff[i : i + K - 1]) for i in range(N - K + 1)))
