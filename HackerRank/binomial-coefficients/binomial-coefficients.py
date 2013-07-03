#!/usr/bin/python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        n, P = list(map(int, sys.stdin.readline().split()))
        
        # We essentially apply Lucas' Theorem, determining the number of non-divisible terms using the base-p expansion of n
        m = n
        k = 1
        
        while m > 0:
            k *= (m % P) + 1
            m //= P
        
        print((n + 1) - k)
