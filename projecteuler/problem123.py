#!/usr/bin/env python

"""
Problem 123:

Let p_n be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when
(p_n - 1)^n + (p_n + 1)^n is divided by p_n^2.

For example, when n = 3, p_3 = 5, and 4^3 + 6^3 = 280 - 5 mod 25.

The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.
"""

from euler import postponed_sieve


N = 10**10

primes = postponed_sieve()
n, p = 1, next(primes)

while (pow(p - 1, n, p * p) + pow(p + 1, n, p * p)) % (p * p) < N:
    n += 1
    p = next(primes)

print(n)
