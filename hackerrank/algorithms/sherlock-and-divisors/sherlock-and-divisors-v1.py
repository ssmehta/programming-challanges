#!/usr/bin/env python

import functools, math, operator as op, sys


def is_prime(n):
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

def prime_factors(n):
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

def tau(n):
    """
    The divisor function, calculating the number of divisors of any integer n.
    If n has k unique prime factors and e_i is the frequency of each prime
    factor, then:
        tau(n) = (e_1 + 1)(e_2 + 1)...(e_k + 1)
    """
    
    return functools.reduce(op.mul, (v + 1 for v in prime_factors(n).values()), 1)


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        print(tau(N // 2) if N % 2 == 0 else 0)
