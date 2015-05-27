#!/usr/bin/env python

import heapq, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    X = sorted(list(map(int, sys.stdin.readline().split())) for _ in range(N))
    
    time = 0
    total_time = 0
    queue = []
    
    while X or queue:
        while X and (not queue or X[0][0] <= time):
            T, L = X.pop(0)
            heapq.heappush(queue, (L, T))
            time = max(time, T)
        
        L, T = heapq.heappop(queue)
        time += L
        total_time += time - T
    
    print(total_time // N)