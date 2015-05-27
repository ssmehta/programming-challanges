#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    max_product = product = sum((i + 1) * a for i, a in enumerate(A))
    total = sum(A)

    for i in range(N):
        product += total - N * A[-i - 1]
        max_product = max(max_product, product)

    print(max_product)