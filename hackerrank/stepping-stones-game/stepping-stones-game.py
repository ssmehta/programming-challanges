#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        a = 8 * N + 1
        b = a**0.5
        
        if int(b)**2 == a:
            print('Go On Bob %d' % ((b - 1) // 2))
        else:
            print('Better Luck Next Time')