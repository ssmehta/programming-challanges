#!/usr/bin/python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    rating = [int(sys.stdin.readline()) for i in range(N)]
    
    candies = [1] * N
    
    for i in range(N - 1):
        if rating[i + 1] > rating[i]:
            candies[i + 1] = candies[i] + 1
    
    for i in reversed(range(N - 1)):
        if rating[i] > rating[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1

    print(sum(candies))
