#!/usr/bin/env python

import sys


def gcd(a, b):
    return b and gcd(b, a % b) or a

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        A, B, C = [int(x) for x in sys.stdin.readline().split()]
        
        # Ensure that A <= B
        A, B = min(A, B), max(A, B)
        domain = 2 * A * B
        
        # Compute the area of the rectangle [0, A] x [0, B] within y <= C - x
        if C >= A + B:
            print('1/1')
        
        else:
            if C <= A:
                cover = C * C
            elif A < C <= B:
                cover = (2 * A * (C - A)) + A**2
            else:
                cover = (2 * A * (C - A)) + (2 * (A + B - C) * (C - B)) + (A + B - C)**2
            
            n = gcd(cover, domain)
            print('%d/%d' % (cover // n, domain // n))
