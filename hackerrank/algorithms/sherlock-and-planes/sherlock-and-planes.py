#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        A = list(map(int, sys.stdin.readline().split()))
        B = list(map(int, sys.stdin.readline().split()))
        C = list(map(int, sys.stdin.readline().split()))
        D = list(map(int, sys.stdin.readline().split()))
        
        AB = [x - y for x, y in zip(B, A)]
        AC = [x - y for x, y in zip(C, A)]
        AD = [x - y for x, y in zip(D, A)]
        
        V = AB[0] * (AC[1] * AD[2] - AC[2] * AD[1])
        V += AB[1] * (AC[0] * AD[2] - AC[2] * AD[0])
        V += AB[2] * (AC[0] * AD[1] - AC[1] * AD[0])
        
        print('YES' if V == 0 else 'NO')