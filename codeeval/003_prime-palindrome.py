#!/usr/bin/env python

"""
Prime Palindrome

Challenge Description:

Write a program to determine the biggest prime palindrome under 1000.

Input sample:

    None

Output sample:

Your program should print the largest palindrome on stdout. i.e.

    929
"""

import math


N = 1000


def is_prime(n):
    """Returns whether the given integer is prime"""
    
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 6
    sqrt_n = int(math.ceil(math.sqrt(n)))
    
    while i <= sqrt_n + 1:
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True


if __name__ == '__main__':
    is_palindrome = lambda s : s == s[::-1]
    
    # Starting from N (= 1000), find the largest prime palindrome
    for n in reversed(range(2, N)):
        s = str(n)
        
        if is_palindrome(str(n)) and is_prime(n):
            print(n)
            break
