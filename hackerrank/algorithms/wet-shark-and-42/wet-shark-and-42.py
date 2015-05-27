#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        S = int(sys.stdin.readline())
        
        n = 2 * S // 42
        
        while 2 * (S + n) // 42 != n:
            n = 2 * (S + n) // 42
            
        print(2 * (S + n) % MOD)