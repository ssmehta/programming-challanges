#!/usr/bin/env python

import sys


def merge_count(ar, left, right):
    i, j, n = 0, 0, 0
    
    while i < len(left) or j < len(right):
        if i == len(left):
            ar[i + j] = right[j]
            j += 1
        elif j == len(right) or left[i] <= right[j]:
            ar[i + j] = left[i]
            i += 1
        else:
            ar[i + j] = right[j]
            j += 1
            n += len(left) - i
    
    return n

def inversion_count(ar):
    if len(ar) <= 1:
        return 0
    
    left = ar[: (len(ar) + 1) // 2]
    right = ar[(len(ar) + 1) // 2 :]
    
    return inversion_count(left) + inversion_count(right) + merge_count(ar, left, right)


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N = int(sys.stdin.readline())
        ar = list(map(int, sys.stdin.readline().split()))
        print(inversion_count(ar))
