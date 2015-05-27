#!/usr/bin/env python

import collections, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        S = sys.stdin.readline().strip()

        # Count the each sorted substring
        substrings = (''.join(sorted(S[j : j + i])) for i in range(1, len(S)) for j in range(len(S) - i + 1))
        substrings = collections.Counter(substrings)

        # Count pairs for each set of anagrams
        print(sum(v * (v - 1) // 2 for v in substrings.values()))