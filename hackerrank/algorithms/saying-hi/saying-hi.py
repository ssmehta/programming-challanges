#!/usr/bin/env python

import re, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    regex = re.compile(r"(^hi\s[^d])", re.IGNORECASE)
    
    for i in range(N):
        s = sys.stdin.readline().strip()
        
        if regex.match(s):
            print(s)
