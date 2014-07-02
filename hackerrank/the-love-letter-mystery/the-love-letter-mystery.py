#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        s = list(sys.stdin.readline().strip())
        print(sum(abs(ord(s[i]) - ord(s[-i - 1])) for i in range(len(s) // 2)))