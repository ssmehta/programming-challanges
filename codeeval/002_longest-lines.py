#!/usr/bin/env python

"""
Longest Lines

Challenge Description:

Write a program to read a multiple line text file and write the 'N' longest lines to stdout. Where the file to be read is specified on the command line.

Input sample:

Your program should read an input file (the first argument to your program). The first line contains the value of the number 'N' followed by multiple lines. You may assume that the input file is formatted correctly and the number on the first line i.e. 'N' is a valid positive integer.e.g.

    2
    Hello World

    CodeEval
    Quick Fox
    A
    San Francisco

NOTE: For solutions in JavaScript, assume that there are 8 lines of input (i.e. line 1 will be N and the next 7 lines will be the input lines

Output sample:

The 'N' longest lines, newline delimited. Do NOT print out empty lines. Ignore all empty lines in the input. Ensure that there are no trailing empty spaces on each line you print. Also ensure that the lines are printed out in decreasing order of length i.e. the output should be sorted based on their length e.g.

    San Francisco
    Hello World
"""

import sys


if __name__ == '__main__':
    lines, lengths = [''], [0]
    
    with open(sys.argv[1]) as f:
        n = int(f.readline())
        
        for line in f:
            line = line.strip()
            
            if len(line) > min(lengths):
                if len(lines) >= n:
                    idx = lengths.index(min(lengths))
                    lines.pop(idx)
                    lengths.pop(idx)
                
                lines.append(line)
                lengths.append(len(line))
        
    for line in [x for (y, x) in sorted(zip(lengths, lines), reverse = True)]:
        print(line)
