#!/usr/bin/env python

"""
Problem 015:

Starting in the top left corner of a 2 x 2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20 x 20 grid?
"""

from euler import choose


N = 20
print(choose(2 * N, N))  # Central binomial coefficient
