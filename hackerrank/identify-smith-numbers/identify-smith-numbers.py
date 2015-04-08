#!/usr/bin/env python

import math, sys


def is_prime(n):
    """Returns whether the given integer is prime"""
    
    if n < 2:
        return False
    elif n == 2 or n == 3 or n == 5:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    
    i = 6
    sqrt_n = int(math.ceil(math.sqrt(n)))
    
    while i <= sqrt_n + 1:
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def get_prime_factors(n):
    """
    Calculates the prime factorization of an integer, returning a dictionary of each prime factor
    and its frequency in the factorization.
    """
    factors = {}
    if n <= 1: return {}
    
    while n != 1:
        if is_prime(n):
            factors[n] = 1
            break
        
        i = 2
        while i <= n:
            j = 0
            while n % i == 0 and n != 1:
                j += 1
                n //= i
            
            if j > 0:
                factors[i] = j
                break
            i += 1
    
    return factors


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    sum_of_digits = lambda N: sum(map(int, str(N)))
    sum_of_prime_factors = sum(v * sum_of_digits(k) for k, v in get_prime_factors(N).items())
    
    print(1 if sum_of_digits(N) == sum_of_prime_factors else 0)