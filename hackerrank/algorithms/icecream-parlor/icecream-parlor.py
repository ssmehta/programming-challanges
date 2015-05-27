#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        M = int(sys.stdin.readline())
        N = int(sys.stdin.readline())
        C = list(map(int, sys.stdin.readline().split()))
        
        for i, c in enumerate(C[:-1]):
            for j in range(i + 1, len(C)):
                if C[j] == M - c:
                    print(i + 1, j + 1)
                    break
