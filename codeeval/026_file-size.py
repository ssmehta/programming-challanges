#!/usr/bin/env python

"""
File Size

Challenge Description:

Print the size of a file in bytes.

Input:

The first argument to your program has the path to the file you need to check the size of.

Output sample:

Print the size of the file in bytes. e.g.

    55
"""

import os, sys

if __name__ == '__main__':
    print(os.stat(sys.argv[1]).st_size)
