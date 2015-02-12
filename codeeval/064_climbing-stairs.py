#!/usr/bin/env python

"""
Climbing Stairs

Challenge Description:

You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer which is the total number of stairs. e.g.

    10
    20

Output sample:

Print out the number of ways to climb to the top of the staircase. e.g.

    89
    10946
"""

import sys


if __name__ == '__main__':
    # See: http://en.wikipedia.org/wiki/Fibonacci_number#Occurrences_in_mathematics
    fib = [1, 1]
    
    with open(sys.argv[1]) as f:
        for line in f:
            n = int(line)
            
            while len(fib) <= n:
                fib.append(fib[-1] + fib[-2])
            
            print(fib[n])
