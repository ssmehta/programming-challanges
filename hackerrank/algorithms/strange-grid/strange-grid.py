#!/usr/bin/env python

import sys


if __name__ == '__main__':
    r, c = list(map(int, sys.stdin.readline().split()))
    
    print((r - 1) // 2 * 10 + 2 * (c - 1) + (r - 1) % 2)