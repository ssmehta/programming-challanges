#!/usr/bin/env python

import sys


# Predefined grid size
N = 5

if __name__ == '__main__':
    # Define positions of MarkZoid and the dirt
    bot = tuple(map(int, input().strip().split()))
    
    dirt = []
    
    for i in range(N):
        for j, s in enumerate(sys.stdin.readline().strip()):
            if s == 'd':
                dirt.append((j, i))
    
    # Find the nearest dirt
    dist = [abs(bot[0] - d[0]) + abs(bot[1] - d[1]) for d in dirt]
    idx = dist.index(min(dist))
    
    # Move or clean
    if bot[0] == dirt[idx][0] and bot[1] == dirt[idx][1]:
        print('CLEAN')
    elif bot[0] == dirt[idx][0]:
        print('DOWN' if bot[1] - dirt[idx][1] < 0 else 'UP')
    else:
        print('RIGHT' if bot[0] - dirt[idx][0] < 0 else 'LEFT')
