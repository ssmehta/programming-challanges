#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        
        if N % 2 == 0:
            print(3 if (N // 2) % 2 == 0 else 4)
        else:
            print(2)
