#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        S = list(map(ord, sys.stdin.readline().strip()))
        
        diff = [abs(x - S[i - 1]) for i, x in enumerate(S) if i > 0]
        print('Funny' if diff == diff[::-1] else 'Not Funny')