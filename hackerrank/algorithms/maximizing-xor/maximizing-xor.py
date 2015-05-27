#!/usr/bin/env python

import sys


if __name__ == '__main__':
    L = int(sys.stdin.readline())
    R = int(sys.stdin.readline())
    
    print(max(A ^ B for A in range(L, R + 1) for B in range(L, R + 1)))