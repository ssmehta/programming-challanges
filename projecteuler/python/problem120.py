#!/usr/bin/env python

"""
Problem 120:

Let r be the remainder when (a - 1)^n + (a + 1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 = 42 mod 49. And
as n varies, so too will r, but for a = 7 it turns out that r_max = 42.

For 3 <= a <= 1000, find Sigma r_max.
"""


print(sum(2 * a * ((a - 1) // 2) for a in range(3, 1001)))
