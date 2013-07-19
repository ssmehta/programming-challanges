#!/usr/bin/env python

"""
Prime Numbers

Challenge Description:

Print out the prime numbers less than a given number N. For bonus points your solution should run in N*(log(N)) time or better. You may assume that N is always a positive integer.

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 4,294,967,295. E.g.

    10
    20
    100

Output sample:

For each line of input, print out the prime numbers less than N, in ascending order, comma delimited. (There should not be any spaces between the comma and numbers) E.g.

    2,3,5,7
    2,3,5,7,11,13,17,19
    2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
"""

import sys


def generate_primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    
    sieve = list(range(3, n + 1, 2))
    root_n = n**0.5
    mid = (n + 1) // 2 - 1
    i = 0
    m = 3
    
    while m <= root_n:
        if sieve[i]:
            j = (m * m - 3) // 2
            sieve[j] = 0
            while j < mid:
                sieve[j] = 0
                j += m
        
        i += 1
        m = 2 * i + 3
    
    return [2] + [p for p in sieve if p]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(','.join(map(str, generate_primes(int(line) - 1))))
