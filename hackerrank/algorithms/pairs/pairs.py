#!/usr/bin/env python

import bisect, sys


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().split()))
    numbers = sorted(map(int, sys.stdin.readline().split()))
    
    total = 0
    
    for n in numbers:
        idx = bisect.bisect_left(numbers, n + K)
        
        if idx < N and numbers[idx] == n + K:
            total += 1
    
    print(total)
