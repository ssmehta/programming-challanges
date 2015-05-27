#!/usr/bin/env python

import sys


MAX_N = 5000
MOD = 1000000009


if __name__ == '__main__':
    # Compute factorials
    factorial = [1]
    for n in range(1, 2 * MAX_N + 1):
        factorial.append(n * factorial[-1] % MOD)

    # Define required functions
    modinv = lambda n: pow(n, MOD - 2, MOD)
    choose = lambda n, k: factorial[n] * modinv(factorial[k] * factorial[n - k]) % MOD
    catalan = lambda n: choose(2 * n, n) * modinv(n + 1) % MOD


    # Solve challenge
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        print(sum(choose(N, k) * catalan(k) for k in range(1, N + 1)) % MOD)