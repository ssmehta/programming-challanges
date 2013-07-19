#!/usr/bin/python

import collections, sys


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    c = collections.Counter(s)
    
    parity = (v % 2 for v in c.values())
    parity_count = collections.Counter(parity)
    
    if 1 in parity_count:
        print('NO' if parity_count[1] > 1 else 'YES')
    else:
        print('YES')
