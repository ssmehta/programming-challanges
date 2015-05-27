#!/usr/bin/env python

import bisect, sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    
    a = []
    len_a = 0
    
    for i in range(n):
        action, x = sys.stdin.readline().split()
        idx = bisect.bisect_left(a, int(x))
        
        # Perform requested action
        if action == 'r':
            if idx >= len_a or a[idx] != int(x):
                print('Wrong!')
                continue
            else:
                del(a[idx])
                len_a -= 1
        elif action == 'a':
            a.insert(idx, int(x))
            len_a += 1
        else:
            print('Wrong!')
            continue
        
        # Print median
        mid = len_a // 2
        
        if len_a == 0:
            print('Wrong!')
        elif len_a % 2:
            print(a[mid])
        else:
            x = a[mid - 1] + a[mid]
            print(x / 2 if x % 2 else x // 2)
