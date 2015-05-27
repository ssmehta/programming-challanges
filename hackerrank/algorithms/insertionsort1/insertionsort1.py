#!/usr/bin/env python

import sys


def print_list(ar):
    print(' '.join(map(str, ar)))

def insertion_sort(ar):
    if len(ar) == 1:
        print_list(ar)
        return(ar)
    else:
        x = ar[-1]
        
        for i in reversed(range(len(ar) - 1)):
            if x < ar[i]:
                ar[i + 1] = ar[i]
                print_list(ar)
                
                if i == 0:
                    ar[0] = x
                    print_list(ar)
                    break
            else:
                ar[i + 1] = x
                print_list(ar)
                break
    
        return(ar)
                
if __name__ == '__main__':
    s = int(sys.stdin.readline())
    ar = list(map(int, sys.stdin.readline().split()))
    
    insertion_sort(ar)
