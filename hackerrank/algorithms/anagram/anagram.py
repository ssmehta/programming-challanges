#!/usr/bin/env python

import collections, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        s = sys.stdin.readline().strip()
        
        if len(s) % 2:
            print(-1)
        else:
            s1, s2 = s[: len(s) // 2], s[len(s) // 2 :]
            c2 = collections.Counter(s2)
            
            replacements = len(s1)
            
            for c in s1:
                if c in c2 and c2[c] > 0:
                    replacements -= 1
                    c2[c] -= 1
            
            print(replacements)
