#!/usr/bin/python

import sys


if __name__ == '__main__':
    V = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    
    print(ar.index(V))
