#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    for i in range(1, N + 1):
        print((N - i) * ' ' + i * '#')