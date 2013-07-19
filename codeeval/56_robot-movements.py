#!/usr/bin/env python

"""
Robot Movements

Challenge Description:

A robot is located at the top-left corner of a 4x4 grid. The robot can move either up, down, left, or right, but can not visit the same spot twice. The robot is trying to reach the bottom-right corner of the grid.

Input sample:

There is no input for this program.

Output sample:

Print out the unique number of ways the robot can reach its destination. (The number should be printed as an integer whole number eg. if the answer is 10 (its not !!), print out 10, not 10.0 or 10.00 etc)
"""


Nx, Ny = 4, 4


def count_routes(grid, startx, starty, endx, endy):
    if grid[starty][startx]:
        return 0
    elif startx == endx and starty == endy:
        return 1
    else:
        # Mark as visited
        next_step = [x[:] for x in grid]
        next_step[starty][startx] = True
        
        n = 0
        
        if startx > 0: n += count_routes(next_step, startx - 1, starty, endx, endy)
        if starty > 0: n += count_routes(next_step, startx, starty - 1, endx, endy)
        if startx < Nx - 1: n += count_routes(next_step, startx + 1, starty, endx, endy)
        if starty < Ny - 1: n += count_routes(next_step, startx, starty + 1, endx, endy)
        
        return n


if __name__ == '__main__':
    grid = [[False for _ in range(Nx)] for _ in range(Ny)]
    
    print(count_routes(grid, 0, 0, Nx - 1, Ny - 1))
