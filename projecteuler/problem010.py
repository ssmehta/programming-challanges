#!/usr/bin/env python

"""
Problem 010:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from euler import generate_primes


N = 2000000
print(sum(generate_primes(N)))
