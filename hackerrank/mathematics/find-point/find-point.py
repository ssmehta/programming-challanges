#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        Px, Py, Qx, Qy = list(map(int, sys.stdin.readline().split()))
        
        print(2 * Qx - Px, 2 * Qy - Py)
