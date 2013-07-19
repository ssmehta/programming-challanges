#!/usr/bin/python

import collections, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N = int(sys.stdin.readline())
        c = list(map(int, sys.stdin.readline().split()))
        
        # Count of each unique card
        count = collections.Counter(c)
        
        # Values to keep track of possible combinations and remaining cards
        n = 0
        combinations = 1
        possible_terms = 0
        
        while True:
            if n in count:
                possible_terms += count[n]
            
            if possible_terms > 0:
                combinations *= possible_terms
                combinations %= 1000000007
                possible_terms -= 1
                n += 1
            else:
                break
        
        print(0 if n < max(c) else combinations)
