#!/usr/bin/env python

"""
Problem 041:

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

from euler import is_prime, itertools


largest_prime = 2

# We only need to consider 7-digit pandigital primes.  If the answer contains
# 8 digits, then 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36, which is divisble by 3,
# so it cannot be prime.  Similarly, adding 9 yields 45, which 3 also divides.
for n in range(2, 8):
    for x in itertools.permutations(range(1, n + 1)):
        p = int(''.join(map(str, x)))
        
        if p > largest_prime and is_prime(p):
            largest_prime = p

print(largest_prime)

