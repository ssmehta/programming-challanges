#!/usr/bin/env python

import itertools, sys


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    
    # Compute rectangle area
    dim = int(len(s)**0.5)
    if dim * dim == len(s):
        x, y = dim, dim
    else:
        x, y = dim, dim + 1
    
    # Produce message array, find its transpose and print
    array = [s[i : i + y] for i in range(0, len(s), y)]
    transpose = itertools.zip_longest(*array, fillvalue = '')
    print(' '.join(''.join(s) for s in transpose))
