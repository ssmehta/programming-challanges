#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
        
        ones = A.count(1)
        twos = A.count(2)
        
        total = 0
        
        # Count the contributions from 1 with each non-1
        total += ones * (N - ones)
        
        # Count the contributions from pairs of 1's
        total += ones * (ones - 1)
        
        # Count the contributions from pairs of 2's
        total += twos * (twos - 1) // 2
        
        print(total)