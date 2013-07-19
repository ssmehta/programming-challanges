#!/usr/bin/python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    # Get the prime factors of N!
    primes = {}
    sieve = list(range(N + 1))
    n = 2
    
    while n < N + 1:
        if sieve[n] > 1:
            primes[n] = 1
            
            k = 2
            while k * n < N + 1:
                while sieve[k * n] % n == 0:
                    sieve[k * n] //= n
                    primes[n] += 1
                k += 1
        n += 1
    
    # Square N!
    for k in primes:
        primes[k] *= 2
    
    # Find number of divisors of (N!)^2
    tau = 1
    for k, v in primes.items():
        tau *= v + 1
        tau %= 1000007
    
    # Number of order-dependent solutions to the Diophantine equation is simply tau((N!)^2)
    print(tau)
