#!/usr/bin/env python

"""
Roman Numerals

Challenge Description:

Many persons are familiar with the Roman numerals for relatively small numbers. The symbols I (capital i), V, X, L, C, D, and M represent the decimal values 1, 5, 10, 50, 100, 500 and 1000 respectively. To represent other values, these symbols, and multiples where necessary, are concatenated, with the smaller-valued symbols written further to the right. For example, the number 3 is represented as III, and the value 73 is represented as LXXIII. The exceptions to this rule occur for numbers having units values of 4 or 9, and for tens values of 40 or 90. For these cases, the Roman numeral representations are IV (4), IX (9), XL (40), and XC (90). So the Roman numeral representations for 24, 39, 44, 49, and 94 are XXIV, XXXIX, XLIV, XLIX, and XCIV, respectively. 

Write a program to convert a cardinal number to a Roman numeral.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    159
    296
    3992

Input numbers are in range [1, 3999]

Output sample:

Print out Roman numerals.

    CLIX
    CCXCVI
    MMMCMXCII
"""

import sys


conv = {
    1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
    100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
}

def decimal_to_roman(n):
    s = ''
    
    if n < 5000:
        for k, v in sorted(conv.items(), reverse = True):
            while n >= k:
                s += v
                n -= k
    
    return s


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(decimal_to_roman(int(line)))
