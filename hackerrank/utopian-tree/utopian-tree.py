#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        height = 1
        
        for i in range(N):
            if i % 2 == 0:
                height *= 2
            else:
                height += 1
            
        print(height)
