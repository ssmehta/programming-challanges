#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N, I = list(map(int, sys.stdin.readline().split()))
    
    # Count astronauts from different countries
    astronauts = [-1] * N
    countries = []
    
    for _ in range(I):
        A, B = list(map(int, sys.stdin.readline().split()))
        
        if astronauts[A] > -1 and astronauts[B] > -1:
            if astronauts[A] != astronauts[B]:
                k = astronauts[B]
                countries[astronauts[A]].extend(countries[k])
                
                for i in countries[k]:
                    astronauts[i] = astronauts[A]
                countries[k] = []
        
        elif astronauts[A] > -1 and astronauts[B] == -1:
            astronauts[B] = astronauts[A]
            countries[astronauts[A]].append(B)
        
        elif astronauts[A] == -1 and astronauts[B] > -1:
            astronauts[A] = astronauts[B]
            countries[astronauts[B]].append(A)
        
        else:
            astronauts[B] = astronauts[A] = len(countries)
            countries.append([A, B])
        
    
    # Count combinations, first from the unpaired astronauts
    unpaired = sum(x == -1 for x in astronauts)
    x = [len(c) for c in countries if c]
    
    total = unpaired * (unpaired - 1) // 2
    total += unpaired * sum(x)
    total += sum(x[i] * x[j] for i in range(len(x) - 1) for j in range(i + 1, len(x)))
    
    print(total)
