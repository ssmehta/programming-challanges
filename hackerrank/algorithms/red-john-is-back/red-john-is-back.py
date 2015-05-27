#!/usr/bin/env python

import sys


C = 4


def generate_primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    
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


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        
        count, n = 1, 1
        
        if N % C == 0:
            count += 1
        
        while N - (n * C) > 0:
            count += choose(N - (C - 1) * n, n)
            n += 1
        
        print(len(generate_primes(count)))