#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    balls = [int(sys.stdin.readline()) for _ in range(N)]
    
    print('%.1f' % (sum(balls) / 2))
