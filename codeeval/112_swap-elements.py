#!/usr/bin/env python

"""
Swap Elements

Challenge Description:

You are given a list of numbers which is supplemented with positions that have to be swapped.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    1 2 3 4 5 6 7 8 9 : 0-8
    1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

As you can see a colon separates numbers with positions. 
Positions start with 0. 
You have to process positions left to right. In the example above (2nd line) first you process 0-1, then 1-3.

Output sample:

Print the lists in the following way.

    9 2 3 4 5 6 7 8 1
    2 4 3 1 5 6 7 8 9 10
"""

import re, sys


if __name__ == '__main__':
    regex = re.compile(r'((\d+)-(\d+))')
    
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                n, s = line.strip().split(' : ')
                n = list(map(int, n.split()))
                
                for _, i, j in regex.findall(s):
                    i, j = int(i), int(j)
                    n[i], n[j] = n[j], n[i]
            
                print(' '.join(map(str, n)))
