#!/usr/bin/env python

"""
Problem 006:

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


N = 100

# Simplified from:
# (\Sigma_{i = 1}^n i)^2 - \Sigma_{i = 1}^n i^2 = [(n / 2)(n + 1)]^2 - (n / 6)(n + 1)(2n + 1)
f = lambda n: (n * (n - 1) * (n + 1) * (3 * n + 2)) // 12

# Alternatively, since N is small
print(sum(range(1, N + 1))**2 - sum(map(lambda n : n * n, range(1, N + 1))))
