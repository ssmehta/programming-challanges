#!/usr/bin/env python

import re, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    regex = re.compile(r"(^[A-Z]{5}\d{4}[A-Z]$)")
    
    for i in range(N):
        pan = sys.stdin.readline().strip()
        print('YES' if regex.match(pan) else 'NO')
