#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, C, M = [int(x) for x in sys.stdin.readline().split()]
        
        total = wrappers = N // C
        
        while wrappers >= M:
            total += wrappers // M
            wrappers = (wrappers % M) + (wrappers // M)
        
        print(total)