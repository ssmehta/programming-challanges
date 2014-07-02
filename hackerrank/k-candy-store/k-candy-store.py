#!/usr/bin/env python

import itertools, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    # Generate Pascal's Triangle
    pascal = [[1], [1, 1]]
    while len(pascal) < 1000:
        row = [(pascal[-1][i] + pascal[-1][i + 1]) % 10**9 for i in range(len(pascal) - 1)]
        pascal.append([1] + row + [1])
    
    # Transpose the triangle
    pascal = [list(filter(None.__ne__, x)) for x in itertools.zip_longest(*pascal)]
    
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        K = int(sys.stdin.readline())
        print(pascal[N - 1][K])
