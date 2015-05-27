#!/usr/bin/env python

import sys


def insertion_sort(ar):
    if len(ar) <= 1:
        print(0)
        return(ar)
    else:
        shifts = 0
        
        for j in range(1, len(ar)):
            for i in reversed(range(j)):
                if ar[i + 1] < ar[i]:
                    ar[i], ar[i + 1] = ar[i + 1], ar[i]
                    shifts += 1
                else:
                    break
        
        print(shifts)
        return(ar)
                
if __name__ == '__main__':
    s = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    insertion_sort(ar)
