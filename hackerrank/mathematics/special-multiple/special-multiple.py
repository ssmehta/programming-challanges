#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = int(sys.stdin.readline())
        
        x = 1
        while int(str(bin(x))[2:].replace('1', '9')) % N != 0:
            x += 1
        
        print(int(str(bin(x))[2:].replace('1', '9')))
