#!/usr/bin/env python

"""
String Rotation

Challenge Description:

You are given two strings. Determine if the second string is a rotation of the first string.

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated strings. E.g.

    Hello,lloHe
    Basefont,tBasefon

Output sample:

Print out True/False if the second string is a rotation of the first. E.g.

    True
    True
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                x, y = line.strip().split(',')
                
                if len(x) != len(y):
                    print('False')
                elif y in x + x:
                    print('True')
                else:
                    print('False')
