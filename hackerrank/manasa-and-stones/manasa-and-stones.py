#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        a = int(sys.stdin.readline())
        b = int(sys.stdin.readline())
        
        print(*sorted(set(x * a + (n - 1 - x) * b for x in range(n))))