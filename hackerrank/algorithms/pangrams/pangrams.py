#!/usr/bin/env python

import string, sys


if __name__ == '__main__':
    s = sys.stdin.readline().strip().lower()
    
    print('pangram' if all(c in s for c in string.ascii_lowercase) else 'not pangram')