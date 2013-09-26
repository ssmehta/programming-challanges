#!/usr/bin/env python

"""
Following Integer

Challenge Description:

Credits: This challenge has appeared in a past google competition

You are writing out a list of numbers.Your list contains all numbers with exactly Di digits in its decimal representation which are equal to i, for each i between 1 and 9, inclusive. You are writing them out in ascending order. For example, you might be writing every number with two '1's and one '5'. Your list would begin 115, 151, 511, 1015, 1051. Given N, the last number you wrote, compute what the next number in the list will be. The number of 1s, 2s, ..., 9s is fixed but the number of 0s is arbitrary.

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10^6

Output sample:

For each line of input, generate a line of output which is the next integer in the list.
"""

import sys


def next_lexographic(n):
    # Find pivot index
    idx = len(n) - 2
    
    while idx > -1 and n[idx] >= n[idx + 1]:
        idx -= 1
    
    
    if idx > -1:
        j = len(n) - 1
        
        while j > idx and n[idx] >= n[j]:
            j -= 1
        
        n[idx], n[j] = n[j], n[idx]
        return n[: idx + 1] + sorted(n[idx + 1:])
    
    else:
        zeros = n.count(0) + 1
        n = sorted(x for x in n if x != 0)
        return [n[0]] + [0] * zeros + n[1:]
        


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                n = list(map(int, line.strip()))
                print(int(''.join(str(i) for i in next_lexographic(n))))
