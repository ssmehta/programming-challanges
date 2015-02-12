#!/usr/bin/env python

import collections, sys


MOD = 1000000007


if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    C = list(map(int, sys.stdin.readline().split()))
    
    count = collections.defaultdict(lambda: 1)
    
    for i in range(M):
        count[B[i]] = (count[B[i]] * C[i]) % MOD
    
    for k, v in count.items():
        for i in range(k - 1, N, k):
            A[i] = (A[i] * v) % MOD
    
    print(*A, sep = ' ')