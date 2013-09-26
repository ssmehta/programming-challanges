#!/usr/bin/env python

"""
Double Squares

Challenge Description:

Credits: This challenge appeared in the Facebook Hacker Cup 2011. 

A double-square number is an integer X which can be expressed as the sum of two perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2. Your task in this problem is, given X, determine the number of ways in which it can be written as the sum of two squares. For example, 10 can only be written as 3^2 + 1^2 (we don't count 1^2 + 3^2 as being different). On the other hand, 25 can be written as 5^2 + 0^2 or as 4^2 + 3^2. 
NOTE: Do NOT attempt a brute force approach. It will not work. The following constraints hold: 
0 <= X <= 2147483647 
1 <= N <= 100

Input sample:

You should first read an integer N, the number of test cases. The next N lines will contain N values of X.

    5
    10
    25
    3
    0
    1

Output sample:

e.g.

    1
    2
    0
    1
    1
"""

import sys


MAX = 2147483647


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        N = int(f.readline())
        
        for _ in range(N):
            n = int(f.readline())
            count = 0
            
            for j in range(int((n // 2)**0.5) + 1):
                k = (n - j * j)**0.5
                if k - int(k) < 1e-15:
                    count += 1
            
            print(count)
