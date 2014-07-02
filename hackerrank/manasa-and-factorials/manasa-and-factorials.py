#!/usr/bin/env python

import math, sys


MAX_N = 10**16
MAX_MULT = int(math.log(MAX_N) / math.log(5)) + 1


if __name__ == '__main__':
    # Multiplicities
    multiplicities = [(i, (5**i - 1) // 4) for i in reversed(range(1, MAX_MULT + 1))]
    

    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        m = 0

        for k, p in multiplicities:
            if p <= n:
                i = n // p
                n -= i * p
                m += i * 5**k

        print(m)
