#!/usr/bin/python

import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    words = ' '.join(sys.stdin.readline().strip() for i in range(N))
    T = int(sys.stdin.readline())
    
    for i in range(T):
        t_us = sys.stdin.readline().strip()
        t_uk = t_us[::-1].replace('z', 's', 1)[::-1]
        
        print(words.count(t_us) + words.count(t_uk))
