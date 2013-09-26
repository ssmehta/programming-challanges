#!/usr/bin/env python

import sys


MOD = 1000000007


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, M = list(map(int, sys.stdin.readline().split()))
            
        # The number of combinations to build a single row
        row_combinations = [1, 1, 2, 4]
        
        # Build row combinations up to this wall's width
        while len(row_combinations) <= M:
            row_combinations.append(sum(row_combinations[-4:]) % MOD)
        
        
        # Compute total combinations for constructing a wall of height N of varying widths
        total = [pow(c, N, MOD) for c in row_combinations]
        
        
        # Find the number of unstable wall configurations for a wall of height N of varying widths
        unstable = [0, 0]
        
        for i in range(2, M + 1):
            unstable.append(sum((total[j] - unstable[j]) * total[i - j] for j in range(1, i)) % MOD)
        
        
        # Print the number of stable wall combinations
        print((total[M] - unstable[M]) % MOD)
