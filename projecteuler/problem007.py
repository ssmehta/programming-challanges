#!/usr/bin/env python

"""
Problem 007:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""

from euler import postponed_sieve


N = 10001

p = postponed_sieve()

for i in range(N - 1):
    next(p)

print(next(p))
