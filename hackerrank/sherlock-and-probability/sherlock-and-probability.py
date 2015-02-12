#!/usr/bin/env python

import fractions, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, K = list(map(int, sys.stdin.readline().split()))
        S = list(map(int, sys.stdin.readline().strip()))
        
        
        x = sum(S[: K + 1])
        pairs = x * (x - 1) // 2
        
        for i in range(1, N - K):
            x -= S[i - 1]
            
            if S[i + K] == 1:
                pairs += x
                x += 1
        

        valid = sum(S) + 2 * pairs
        total = N**2

        gcd = fractions.gcd(valid, total)
        
        print('%d/%d' % (valid // gcd, total // gcd))