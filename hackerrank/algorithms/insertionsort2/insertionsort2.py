#!/usr/bin/env python

import sys


def print_list(ar):
    print(' '.join(map(str, ar)))

def insertion_sort(ar):
    if len(ar) == 1:
        print_list(ar)
        return(ar)
    else:
        for j in range(1, len(ar)):
            for i in reversed(range(j)):
                if ar[i + 1] < ar[i]:
                    ar[i], ar[i + 1] = ar[i + 1], ar[i]
                else:
                    break
            
            print_list(ar)
        
        return(ar)
                
if __name__ == '__main__':
    s = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    
    insertion_sort(ar)
