#!/usr/bin/python

import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    for i in range(N):
        s = sys.stdin.readline().strip()
        
        # Didn't realize this challenge came under regular expressions...oh well
        if s.startswith('hackerrank') and s.endswith('hackerrank'):
            print(0)
        elif s.startswith('hackerrank'):
            print(1)
        elif s.endswith('hackerrank'):
            print(2)
        else:
            print(-1)
