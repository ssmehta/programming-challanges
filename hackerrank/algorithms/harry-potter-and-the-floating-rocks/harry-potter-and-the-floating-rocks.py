#!/usr/bin/env python

import fractions, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        
        if dx == 0:
            print(dy - 1)
        elif dy == 0:
            print(dx - 1)
        else:
            print(fractions.gcd(dx, dy) - 1)