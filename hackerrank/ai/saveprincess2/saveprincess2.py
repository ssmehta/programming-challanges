#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    mario = tuple(map(int, input().strip().split()))
    
    # Find the location of Princess Peach
    princess = -1
    
    for i in range(N):
        s = sys.stdin.readline().strip()
        
        if 'p' in s:
            princess = (s.find('p'), i)
    
    # Find next move
    dx, dy = mario[0] - princess[0], mario[1] - princess[1]
    
    if dx == 0:
        print('DOWN' if dy < 0 else 'UP')
    else:
        print('RIGHT' if dx < 0 else 'LEFT')
