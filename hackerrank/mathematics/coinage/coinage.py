#!/usr/bin/env python

import sys


COINS = [1, 2, 5, 10]


def count(memo, n, k):
    if (n, k) in memo:
        return memo[(n, k)]
    
    elif k == 0:
        return int(n <= A[0] * COINS[0] and n % COINS[0] == 0)
    
    else:
        i, total = 0, 0
        
        while i <= A[k] and i * COINS[k] <= n:
            total += count(memo, n - i * COINS[k], k - 1)
            i += 1
        
        memo[(n, k)] = total
        return total


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
        
        memo = {}
        print(count(memo, N, len(COINS) - 1))
