#!/usr/bin/env python

import sys


MAX_N = 10**10


if __name__ == '__main__':
    # Generate Fibonacci Numbers
    fibonacci = [0, 1]
    
    while fibonacci[-1] < MAX_N:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])


    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        print('IsFibo' if N in fibonacci else 'IsNotFibo')
