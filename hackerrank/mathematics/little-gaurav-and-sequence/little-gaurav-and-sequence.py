#!/usr/bin/env python

import math, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        
        # Value of interior sum
        n = 7 * (pow(4, N + 1, 10) - 1) % 10
        
        # Value of outer sum
        max_i = math.log(N) / math.log(2)
        m = sum(pow(2, 2**i, 10) for i in range(int(max_i) + 1))
        
        print(n * m % 10)