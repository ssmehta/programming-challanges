#!/usr/bin/python

import collections, math, sys


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    c = collections.Counter(s)
    
    n = math.factorial(sum(v // 2 for v in c.values()))
    
    for v in c.values():
        if v > 1:
            n //= math.factorial(v // 2)
    
    print(n % 1000000007)
