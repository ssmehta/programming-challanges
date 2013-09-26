#!/usr/bin/env python

"""
Minimum Coins

Challenge Description:

You are given 3 coins of value 1, 3 and 5. You are also given a total which you have to arrive at. Find the minimum number of coins to arrive at it.

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer number which represents the total you have to arrive at. E.g.

    11
    20

Output sample:

Print out the minimum number of coins required to arrive at the total. E.g.

    3
    4
"""

import sys


if __name__ == '__main__':
    coins = [1, 3, 5]
    
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                n = int(line)
                total = 0
                
                for x in sorted(coins, reverse = True):
                    total += n // x
                    n %= x
                
                print(total)
