#!/usr/bin/env python

import itertools, os, sys


def pairwise(s):
    a, b = itertools.tee(s)
    next(b, None)
    return(zip(a, b))

def string_similarity(s):
    # Compute limited, sorted suffix array and LCP between successive suffixes
    # Followed techniques used by http://stackoverflow.com/a/13574862
    
    suffixes = sorted(s[i:] for i in range(len(s)) if s[i] == s[0])
    lcp = list(map(len, map(os.path.commonprefix, pairwise(suffixes))))
    
    idx = suffixes.index(s)
    similarities = len(s)
    
    # Back count
    if idx > 0:
        similarities += lcp[idx - 1]
        min_count = lcp[idx - 1]
        
        for i in reversed(range(idx - 1)):
            if lcp[i] < min_count:
                min_count = lcp[i]
            similarities += min_count
    
    # Forward count
    if idx < len(lcp):
        similarities += lcp[idx]
        min_count = lcp[idx]
        
        for i in range(idx + 1, len(lcp)):
            if lcp[i] < min_count:
                min_count = lcp[i]
            similarities += min_count
    
    return(similarities)

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        s = sys.stdin.readline().strip()
        print(string_similarity(s))
        if i == 1: break
