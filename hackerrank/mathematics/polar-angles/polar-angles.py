#!/usr/bin/env python

import math, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    P = []
    
    for _ in range(N):
        x, y = list(map(int, sys.stdin.readline().split()))
        P.append(((math.atan2(y, x) + 2 * math.pi) % (2 * math.pi), x**2 + y**2, x, y))
    
    P.sort()
    
    for theta, dist, x, y in P:
        print(x, y)