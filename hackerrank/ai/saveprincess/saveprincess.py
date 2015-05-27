#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    # Find the locations of Mario and Princess Peach
    mario, princess = -1, -1
    
    for i in range(N):
        s = sys.stdin.readline().strip()
        
        if 'm' in s:
            mario = (s.find('m'), i)
        if 'p' in s:
            princess = (s.find('p'), i)
    
    # Generate path
    path = []
    path.append('DOWN' if mario[1] - princess[1] < 0 else 'UP')
    path.append('RIGHT' if mario[0] - princess[0] < 0 else 'LEFT')
    path *= N // 2
    
    # Print path
    for s in path:
        print(s)
