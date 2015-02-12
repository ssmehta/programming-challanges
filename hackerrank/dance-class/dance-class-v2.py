#!/usr/bin/env python

import decimal, sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        i = int(sys.stdin.readline())
        print('even' if int(decimal.Decimal(i).sqrt()) % 2 == 0 else 'odd')