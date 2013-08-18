#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N = int(sys.stdin.readline())
        prices = list(map(int, sys.stdin.readline().split()))
        
        change = prices[:]
        for i in reversed(range(N - 1)):
            change[i] = max(prices[i], change[i + 1])
        
        print(sum(max(0, change[i] - prices[i]) for i in range(N)))
