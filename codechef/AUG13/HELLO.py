#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        D, U, N = [f(v) for f, v in zip((float, int, int), sys.stdin.readline().split())]
        M_min, R_min, C_min, idx = 1, D, 0, 0
        
        for i in range(1, N + 1):
            M, R, C = [f(v) for f, v in zip((int, float, int), sys.stdin.readline().split())]
            
            if M_min * (M * R * U + C) < M * (M_min * R_min * U + C_min):
                M_min = M
                R_min = R
                C_min = C
                idx = i
        
        print(idx)
