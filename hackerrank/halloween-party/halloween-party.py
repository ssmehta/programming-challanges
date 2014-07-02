#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        K = int(sys.stdin.readline())
        print((K // 2) * (K - (K // 2)))
