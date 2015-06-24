#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    pascal = [[1], [1, 1]]
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        
        while n >= len(pascal):
            row = [(pascal[-1][i] + pascal[-1][i + 1]) % 10**9 for i in range(len(pascal) - 1)]
            pascal.append([1] + row + [1])
        
        print(*pascal[n], sep = ' ')
