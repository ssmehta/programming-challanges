#!/usr/bin/env python

import math, random, sys


def is_probable_prime(n, k = 7):
    """
    Use Rabin-Miller algorithm to return True (n is probably prime)
    or False (n is definitely composite).
    http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing
    """

    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    
    elif n & 1 == 0:
        return False
    
    else:
        s, d = 0, n - 1

        while d & 1 == 0:
            s, d = s + 1, d >> 1

    # Use random.randint(2, n - 2) for very large numbers
    for a in random.sample(range(2, n - 2), min(n - 4, k)):
        x = pow(a, d, n)

        if x != 1 and x + 1 != n:
            for r in range(1, s):
                x = pow(x, 2, n)

                if x == 1:
                    return False  # composite for sure
                elif x == n - 1:
                    a = 0  # so we know loop didn't continue to end
                    break  # could be strong liar, try another a
        
            if a:
                return False  # composite if we reached end of this loop

    return True


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    """
    The strong Goldbach conjecture implies that if N is even, it can be
    expressed as the sum of 2 primes.  This has been verified up to
    4 x 10^18 (http://mathworld.wolfram.com/GoldbachConjecture.html).
    """
    for _ in range(T):
        N, K = list(map(int, sys.stdin.readline().split()))

        
        if N < 2 * K:
            print('No')
        
        elif K == 1:
            print('Yes' if is_probable_prime(N) else 'No')
        
        elif K == 2:
            if N % 2 == 0:
                print('Yes')
            else:
                print('Yes' if is_probable_prime(N - 2) else 'No')

        else:
            print('Yes')