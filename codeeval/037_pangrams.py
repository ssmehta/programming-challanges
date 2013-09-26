#!/usr/bin/env python

"""
Pangrams

Challenge Description:

The sentence 'A quick brown fox jumps over the lazy dog' contains every single letter in the alphabet. Such sentences are called pangrams. You are to write a program, which takes a sentence, and returns all the letters it is missing (which prevent it from being a pangram). You should ignore the case of the letters in sentence, and your return should be all lower case letters, in alphabetical order. You should also ignore all non US-ASCII characters.In case the input sentence is already a pangram, print out the string NULL

Input sample:

Your program should accept as its first argument a filename. This file will contain several text strings, one per line. Ignore all empty lines. eg.

A quick brown fox jumps over the lazy dog
A slow yellow fox crawls under the proactive dog
Output sample:

Print out all the letters each string is missing in lowercase, alphabetical order .e.g.

NULL
bjkmqz
"""

import sys


alphabet = 'abcdefghijklmnopqrstuvwxyz'

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                line = line.lower().strip()
                missing = [c for c in alphabet if c not in line]
                print(''.join(missing) if missing else 'NULL')
