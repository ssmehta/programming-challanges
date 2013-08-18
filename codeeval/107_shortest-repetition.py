#!/usr/bin/env python

"""
Shortest Repetition

Challenge Description:

Write a program to determine the shortest repetition in a string. 
A string is said to have period p if it can be formed by concatenating one or more repetitions of another string of length p. For example, the string "xyzxyzxyzxyz" has period 3, since it is formed by 4 repetitions of the string "xyz". It also has periods 6 (two repetitions of "xyzxyz") and 12 (one repetition of "xyzxyzxyzxyz").

Input sample:

Your program should accept as its first argument a path to a filename. Each line will contain a string of up to 80 non-blank characters. E.g.

    abcabcabcabc
    bcbcbcbcbcbcbcbcbcbcbcbcbcbc
    dddddddddddddddddddd

Output sample:

Print out the smallest period of the input string. E.g.

    3
    2
    1
"""

import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            
            length = 1
            s = line[0]
            
            while True:
                if len(line) % length == 0:
                    is_repetition = True
                    
                    for i in range(0, len(line), length):
                        if s != line[i : i + length]:
                            is_repetition = False
                            break
                    
                    if is_repetition:
                        break
                
                length += 1
                s = line[:length]
            
            print(length)
