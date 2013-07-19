#!/usr/bin/python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print(sum(1 for i in range(N) if 'hackerrank' in sys.stdin.readline().strip().lower()))
