#!/usr/bin/env python

import sys


if __name__ == '__main__':
    D_a, M_a, Y_a = list(map(int, sys.stdin.readline().split()))
    D_e, M_e, Y_e = list(map(int, sys.stdin.readline().split()))
    
    if Y_a < Y_e or (Y_a == Y_e and M_a < M_e) or (Y_a == Y_e and M_a == M_e and D_a <= D_e):
        print(0)
    elif Y_a == Y_e and M_a == M_e:
        print(15 * (D_a - D_e))
    elif Y_a == Y_e:
        print(500 * (M_a - M_e))
    else:
        print(10000)