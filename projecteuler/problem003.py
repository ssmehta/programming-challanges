#!/usr/bin/env python

"""
Problem 003:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 317584931803?
"""

from euler import get_prime_factors


N = 600851475143
print(max(get_prime_factors(N).keys()))
