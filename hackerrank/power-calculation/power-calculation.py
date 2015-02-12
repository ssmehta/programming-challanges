#!/usr/bin/env python

import itertools, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        K, N = list(map(int, sys.stdin.readline().split()))

        x = list(itertools.accumulate(pow(i, N, 100) for i in range(100)))
        print('%02d' % (((K // 100) * x[-1] + x[K % 100]) % 100))