#!/usr/bin/env python

import sys


MAX_K = 1000
MOD = 1000000007


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a):
    g, x, y = egcd(a, MOD)
    return x % MOD


def pascal(n, memo = [[1]]):
    while len(memo) <= n:
        memo.append(list(map(sum, zip([0] + pascal(n - 1), pascal(n - 1) + [0]))))

    return memo[n]

def choose(n, k):
    return pascal(n)[k]

def bernoulli(n, memo = [1]):
    if n >= len(memo):
        if n == 1:
            memo.append(-modinv(n + 1) % MOD)
        elif n % 2 == 1 and n > 1:
            memo.append(0)
        else:
            x = choose(n + 1, 1) * bernoulli(1)
            x += sum(choose(n + 1, i) * bernoulli(i) for i in range(0, n, 2))
            memo.append(-x * modinv(n + 1) % MOD)

    return memo[n]


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        n, K = list(map(int, sys.stdin.readline().split()))

        x = sum(pow(-1, i) * choose(K + 1, i) * bernoulli(i) * pow(n, K + 1 - i, MOD) for i in range(K + 1))
        print(x * modinv(K + 1) % MOD)
