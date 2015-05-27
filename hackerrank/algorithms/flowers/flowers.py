#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N, K = list(map(int, sys.stdin.readline().split()))
    c = sorted(map(int, sys.stdin.readline().split()))
    
    total = 0
    purchased = 0
    friends = [0] * K
    
    while len(c) > 0:
        total += (friends[purchased % len(friends)] + 1) * c.pop()
        friends[purchased % len(friends)] += 1
        purchased += 1
    
    print(total)
