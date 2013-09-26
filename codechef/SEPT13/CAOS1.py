#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        R, C = [int(x) for x in sys.stdin.readline().split()]
        X = max(R, C)
        
        grid = [list(sys.stdin.readline().strip()) for _ in range(R)]
        cpcs = [[X] * C for _ in range(R)]
        
        for i in range(R):
            left = right = 0
            
            for j in range(C):
                if grid[i][j] == '#':
                    left = 0
                else:
                    cpcs[i][j] = min(cpcs[i][j], left)
                    left += 1
                
                if grid[i][-j - 1] == '#':
                    right = 0
                else:
                    cpcs[i][-j - 1] = min(cpcs[i][-j - 1], right)
                    right += 1
        
        for j in range(C):
            top = bottom = 0
            
            for i in range(R):
                if grid[i][j] == '#':
                    top = 0
                else:
                    cpcs[i][j] = min(cpcs[i][j], top)
                    top += 1
                
                if grid[-i - 1][j] == '#':
                    bottom = 0
                else:
                    cpcs[-i - 1][j] = min(cpcs[-i - 1][j], bottom)
                    bottom += 1
        
        print(sum(sum(1 for x in row if 1 < x and x < X) for row in cpcs))
