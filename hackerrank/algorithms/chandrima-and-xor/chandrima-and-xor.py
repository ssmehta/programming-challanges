#!/usr/bin/env python

import functools, operator as op, sys


MAX = 10**18
MOD = 1000000007


# Generate Fibonacci numbers
# Start with 1 so that FIBONACCI[0] corresponds to 2^0
FIBONACCI = [1, 2]
while FIBONACCI[-1] <= MAX:
    FIBONACCI.append(FIBONACCI[-1] + FIBONACCI[-2])

# Pre-calculate powers of 2
POWERS = [pow(2, i) for i in range(len(FIBONACCI))]


def zeckendorf_number(n):
    """Calculate the nth Zeckendorf number from a precalculated set of
    Fibonacci numbers.  Given in a function instead for the speedup
    required to complete the challenge.
    See: http://stackoverflow.com/q/11241523/406772"""

    result = 0

    for i in reversed(range(len(FIBONACCI))):
        if n >= FIBONACCI[i]:
            result += POWERS[i]
            n -= FIBONACCI[i]
    
    return result

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    print(functools.reduce(op.xor, (zeckendorf_number(a) for a in A)) % MOD)