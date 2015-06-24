#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print(sum(map(int, sys.stdin.readline().split())))