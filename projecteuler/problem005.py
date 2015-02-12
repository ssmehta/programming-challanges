#!/usr/bin/env python

"""
Problem 005:

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from
1 to 20?
"""

from euler import get_prime_factors, op, reduce


N = 20

factors = {}

for n in range(1, N + 1):
    for k, v in get_prime_factors(n).items():
        if k in factors:
            if v > factors[k]:
                factors[k] = v
        else:
            factors[k] = v

print(reduce(op.mul, [k**v for k, v in factors.items()], 1))
