#!/usr/bin/env python

import math, sys


MOD = 1000000007


def rwh_primes2(n):
    """Input n>=6, Returns a list of primes, 2 <= p < n
    http://stackoverflow.com/a/2068548/406772"""

    if n < 3:
        return []
    elif n == 3:
        return [2]
    elif n < 6:
        return [2, 3]

    correction = (n % 6 > 1)
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]

    sieve = [True] * (n // 3)
    sieve[0] = False

    for i in range(int(n**0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3) :: 2 * k] = [False] * ((n // 6 - (k * k) // 6 - 1) // k + 1)
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3 :: 2 * k] = [False] * ((n // 6 - (k * k + 4 * k - 2 * k * (i & 1)) // 6 - 1) // k + 1)
    
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    N, M = min(N, M), max(N, M)

    primes = rwh_primes2(M + 1)
    product = 1
    
    for p in primes:
        n = 0
        k = p
        
        while k <= N:
            n += (N // k) * (M // k)
            k *= p
        
        product *= pow(p, n, MOD)
        product %= MOD
        
    print(product)