#!/usr/bin/env python

import itertools, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        S = sys.stdin.readline().strip()
        
        combinations = (itertools.combinations(S, n) for n in range(1, N + 1))
        for x in sorted(itertools.chain.from_iterable(combinations)):
            print(''.join(x))
