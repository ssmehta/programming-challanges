#!/usr/bin/env python

import functools, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    rocks = [sys.stdin.readline().strip() for _ in range(N)]
    
    print(len(functools.reduce(set.intersection, map(set, rocks))))
