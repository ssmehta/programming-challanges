#!/usr/bin/env python

import sys


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inv(a, m):
    g, x, y = egcd(a, m)
    
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        A, B, X = list(map(int, sys.stdin.readline().split()))
        
        if B < 0:
            A = mod_inv(A, X)
        
        print(pow(A, abs(B), X))