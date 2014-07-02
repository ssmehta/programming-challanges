#!/usr/bin/env python

import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    array = sorted(map(int, sys.stdin.readline().split()))
    
    min_diff = min(b - a for a, b in zip(array, array[1:]))
    print(*sum(([a, b] for a, b in zip(array, array[1:]) if b - a == min_diff), []))