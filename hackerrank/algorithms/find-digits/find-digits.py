#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        digits = list(map(int, str(N)))
        
        print(sum(digits.count(k) for k in range(1, 10) if k in digits and N % k == 0))
