#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, C, M = [int(x) for x in sys.stdin.readline().split()]
        
        n = k = N // C
        
        while k >= M:
            n += k // M
            k = (k % M) + (k // M)
        
        print(n)
