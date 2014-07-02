#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, K = list(map(int, sys.stdin.readline().split()))
        
        # Loop over all multiples of K less than 2N:
        # If nK <= N:
        #     add (nK - 1) // 2 pairs
        # Else:
        #     add (nK - 1) // 2 - (k - N - 1) pairs
        
        total = 0
        a = N // K + 1
        b = (2 * N) // K - (1 if (2 * N) % K == 0 else 0)
        
        if K % 2 == 0:
            total += K * b * (b + 1) // 4 - b
        else:
            if b % 2 == 0:
                total += K * b * (b + 2) // 8 - b // 2
                total += K * b * (b + 2) // 8 - b * (K + 1) // 4
            else:
                total += K * (b - 1) * (b + 1) // 8 - (b - 1) // 2
                total += K * (b + 1) * (b + 3) // 8 - (b + 1) * (K + 1) // 4
        
        total -= (b - a + 1) * ((a + b) * K - 2 * (N + 1)) // 2
        
        print(total)
