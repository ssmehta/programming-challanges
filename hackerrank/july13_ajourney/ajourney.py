#!/usr/bin/python

import decimal, math, sys


decimal.getcontext().prec = 25
log2 = decimal.Decimal(2).log10()

num_digits = lambda n : 1 + int(n * log2)
sum_digits = lambda n : sum(map(int, str(n)))

def first_digits(n, m):
    if m > num_digits(n):
        m = num_digits(n)
    
    x = 10**(n * log2 - (num_digits(n) - m))
    return int(x)

def last_digits(n, m):
    if m > num_digits(n):
        m = num_digits(n)
    
    powers_map = {0: 1, 1: 2}
    mod = 10**m
    
    while max(powers_map) <= n // 2 + 1:
        k = max(powers_map)
        powers_map[2 * k] = powers_map[k]**2
        powers_map[2 * k] %= mod
    
    product = 1
    
    while n > 0:
        k = max(filter(lambda x : x <= n, powers_map))
        n -= k
        product *= powers_map[k]
        product %= mod
    
    return product


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N, K = list(map(int, sys.stdin.readline().split()))
        print(first_digits(N - 1, K) + last_digits(N - 1, K))
