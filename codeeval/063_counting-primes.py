#!/usr/bin/env python

"""
Counting Primes

Challenge Description:

Given two integers N and M, count the number of prime numbers between N and M (both inclusive)

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g.

    2,10
    20,30

Output sample:

Print out the number of primes between N and M (both inclusive)

    4
    2
"""

import sys


def postponed_sieve():
    # http://stackoverflow.com/a/10733621/406772
    yield 2; yield 3; yield 5; yield 7;
    
    def add(D, x, s):
        while x in D:
            x += s
        D[x] = s
    
    # ActiveState Recipe 2002
    D = {}
    ps = (p for p in postponed_sieve())
    p = next(ps) and next(ps)
    q = p * p
    c = 9
    
    while True:
        if c not in D:
            if c < q:
                yield c
            else:
                add(D, c + 2 * p, 2 * p)
                p = next(ps)
                q = p * p
        else:
            s = D.pop(c)
            add(D, c + s, s)
        c += 2


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                N, M = [int(s) for s in line.split(',')]
                primes  = postponed_sieve()
                p = primes.next()
                
                while p < N:
                    p = primes.next()
                
                n = 0
                while p <= M:
                    n += 1
                    p = primes.next()
                
                print(n)
