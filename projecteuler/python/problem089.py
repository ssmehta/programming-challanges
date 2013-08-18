#!/usr/bin/env python

"""
Problem 089:

The rules for writing Roman numerals allow for many ways of writing each number
(see About Roman Numerals...). However, there is always a "best" way of writing
a particular number.

For example, the following represent all of the legitimate ways of writing the
number sixteen:

    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI

The last example being considered the most efficient, as it uses the least
number of numerals.

The 11K text file, roman.txt, contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; that is, they are arranged in
descending units and obey the subtractive pair rule (see About Roman Numerals...
for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal
form.

Note: You can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.
"""


conv = {
    1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
    100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
}

def parse_roman_numeral(s):
    n = 0
    
    for k, v in sorted(conv.items(), reverse = True):
        while s.startswith(v):
            n += k
            s = s[len(v):]
    
    return n
            
def decimal_to_roman_numeral(n):
    s = ''
    
    if n < 5000:
        for k, v in sorted(conv.items(), reverse = True):
            while n >= k:
                s += v
                n -= k
    
    return s


X = [s.strip() for s in open('problem089-roman.txt').readlines()]
Y = [decimal_to_roman_numeral(parse_roman_numeral(s)) for s in X]

print(sum(len(x) - len(y) for x, y in zip(X, Y)))
