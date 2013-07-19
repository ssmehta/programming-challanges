#!/usr/bin/python

import sys


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().split()))
    profits = [int(sys.stdin.readline()) for i in range(N)]
    
    total = sum(profits)
    
    if K == N:
        print(total)
    else:
        x = profits[: K + 1]
        
        min_value = min(x)
        min_index = x.index(min_value)
        
        for i in range(K + 1, N):
            if i - min_index >= K:
                min_value = min(x[i - (K + 1) : i + 1])
                min_index = x.index(min_value)
            
            x.append(min_value + profits[i])
            
            if x[i] < min_value:
                min_value = x[i]
                min_index = i
        
        print(total - min(x[N - (K + 1) :]))
