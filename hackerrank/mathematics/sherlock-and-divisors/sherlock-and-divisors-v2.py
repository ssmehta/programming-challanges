#!/usr/bin/env python

import math, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())

        if N % 2 == 1:
            print(0)
        else:
            print((int(N**0.5)**2 == N) + sum((i % 2 == 0) + ((N // i) % 2 == 0) for i in range(1, math.ceil(N**0.5)) if N % i == 0))