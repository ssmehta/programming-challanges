#!/usr/bin/env python

import itertools, sys


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def base_coefficients(n, base):
    coefficients = []
    
    while n > 0:
        coefficients.append(n % base)
        n //= base
    
    return coefficients

def choose(n, k):
    if k < 0 or k > n:
        return 0
    
    else:
         p, q = 1, 1
         
         for i in range(1, min(k, n - k) + 1):
            p *= n
            q *= i
            n -= 1
         
         return p // q

def lucas_theorem(n, k, p):
    x = itertools.zip_longest(base_coefficients(n, p), base_coefficients(k, p), fillvalue = 0)
    product = 1
    
    for n_i, k_i in x:
        product = (product * choose(n_i, k_i)) % p
    
    return product
    
    
if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, R, M = list(map(int, sys.stdin.readline().split()))

        primes = [p for p in PRIMES if M % p == 0]
        total = 0
        
        for p in primes:
            total += (lucas_theorem(N, R, p) * (M // p) * pow(M // p, p - 2, p)) % M
        
        print(total % M)