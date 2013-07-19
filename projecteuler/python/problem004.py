#!/usr/bin/env python

"""
Problem 004:

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


print(max(i * j for i in range(1, 1000) for j in range(1, 1000) if str(i * j) == str(i * j)[::-1]))
