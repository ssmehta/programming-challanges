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


if __name__ == '__main__':
    # Generate Pascal's triangle
    pascal = [[1]]
    
    while len(pascal) <= MAX_K + 1:
        n = len(pascal)
        pascal.append(list(map(sum, zip([0] + pascal[-1], pascal[-1] + [0]))))
    
    
    # Generate Bernouli numbers
    bernoulli = [1]
    
    while len(bernoulli) <= MAX_K:
        n = len(bernoulli)
        
        if n == 1:
            bernoulli.append(-modinv(n + 1) % MOD)
        elif n % 2 == 1:
            bernoulli.append(0)
        else:
            x = pascal[n + 1][1] * bernoulli[1]
            x += sum(pascal[n + 1][i] * bernoulli[i] for i in range(0, n, 2))
            bernoulli.append(-x * modinv(n + 1) % MOD)
    
    
    # Solve challenge
    T = int(sys.stdin.readline())

    for _ in range(T):
        n, K = list(map(int, sys.stdin.readline().split()))

        x = sum(pow(-1, i) * pascal[K + 1][i] * bernoulli[i] * pow(n, K + 1 - i, MOD) for i in range(K + 1))
        print(x * modinv(K + 1) % MOD)
