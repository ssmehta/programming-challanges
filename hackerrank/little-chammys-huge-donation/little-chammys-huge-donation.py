#!/usr/bin/env python

import sys


square_pyramidal = lambda n: (2 * n**3 + 3 * n**2 + n) // 6


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        X = int(sys.stdin.readline())
        L, R = 1, 1000000
        
        while L < R:
            n = (L + R) // 2
            
            if square_pyramidal(n) < X:
                L = n + 1
            else:
                R = n
        
        print(L if square_pyramidal(L) <= X else L - 1)