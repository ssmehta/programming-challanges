#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n, m = map(int, sys.stdin.readline().split())
        P = map(int, sys.stdin.readline().split())
        rooms = [sorted(map(int, sys.stdin.readline().split())[1:]) for _ in range(n)]
        
        print sum(rooms[p].pop() for p in P if rooms[p])
