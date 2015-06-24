#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    
    print(len([a for a in A if a > 0]) / N)
    print(len([a for a in A if a < 0]) / N)
    print(len([a for a in A if a == 0]) / N)