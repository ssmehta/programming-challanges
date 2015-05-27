#!/usr/bin/env python

import sys


if __name__ == '__main__':
    N, M = list(map(int, sys.stdin.readline().split()))
    T = [int(sys.stdin.readline(), 2) for _ in range(N)]
    
    max_topics, num_teams = 0, 0
    
    for i in range(len(T) - 1):
        for j in range(i + 1, len(T)):
            topics = bin(T[i] | T[j]).count('1')
            
            if(topics == max_topics):
                num_teams += 1
            if(topics > max_topics):
                max_topics = topics
                num_teams = 1
    
    print(max_topics)
    print(num_teams)