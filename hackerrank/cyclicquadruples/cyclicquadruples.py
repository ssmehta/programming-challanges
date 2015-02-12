#!/usr/bin/env python

import functools, itertools, operator as op, sys


MOD = 1000000007
N = 4


class Interval:
    def __init__(self, L, R):
        self.L = L
        self.R = R
    
    def __len__(self): 
        if self.L is not None and self.R is not None:
            return self.R - self.L + 1
        else:
            return 0
    
    def __repr__(self):
        return '[%d, %d]' % (self.L, self.R)
    
    def overlaps(self, I):
        if self and I: return (self.L <= I.R) and (self.R >= I.L)
        else: return False
    
    def intersect(self, I):
        if self and I and self.overlaps(I): return Interval(max(self.L, I.L), min(self.R, I.R))
        else: return Interval(None, None)


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        I = [Interval(*x) for x in zip(*[map(int, sys.stdin.readline().split())] * 2)]
        
        # Total possibilities
        total = functools.reduce(op.mul, map(len, I))

        # Remove all cases with consecutive matching values
        for i in range(N):
            total -= len(I[i].intersect(I[(i + 1) % N])) * len(I[(i + 2) % N]) * len(I[(i + 3) % N])
        
        for i in range(N):
            total += len(I[i].intersect(I[(i + 1) % N]).intersect(I[(i + 2) % N])) * len(I[(i + 3) % N])

        for i in range(N // 2):
            total += len(I[i].intersect(I[(i + 1) % N])) * len(I[(i + 2) % N].intersect(I[(i + 3) % N]))
        
        for i in range(N):
            total -= len(I[i].intersect(I[(i + 1) % N]).intersect(I[(i + 2) % N]).intersect(I[(i + 3) % N]))
        
        total += len(I[0].intersect(I[1]).intersect(I[2]).intersect(I[3]))
        
        print(total % MOD)