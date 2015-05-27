#!/usr/bin/env python

import sys


def string_similarity(s):
    """Computes the string similarity using a simplified Z Algorithm:
    http://codeforces.com/blog/entry/3107
    http://binfalse.de/2010/09/advanced-searching-via-z-algorithm/
    """
    
    l, r, n = 0, 0, len(s)
    z = [0] * n
    
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        
        else:
            # Update Z-box bounds
            l = i
            if i > r:
                r = i
            
            while r < n and s[r - l] == s[r]:
                r += 1
            
            z[i] = r - l
            r -= 1
            
    # Return the total number of string similarities
    return n + sum(z)


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        print(string_similarity(sys.stdin.readline().strip()))
