#!/usr/bin/env python

import collections, sys


if __name__ == '__main__':
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    
    a = collections.Counter(A)
    b = collections.Counter(B)
    
    length = sum(min(a[c], b[c]) for c in (set(A) & set(B)))
    print((len(A) - length) + (len(B) - length))