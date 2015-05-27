#!/usr/bin/env python

import re, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    for i in range(N):
        segs = re.split(r'[-\s]', sys.stdin.readline().strip())
        
        # Tackle the case when the number is split
        if len(segs) > 3:
            segs[2] = ''.join(segs[2:])
        
        print('CountryCode=%s,LocalAreaCode=%s,Number=%s' % tuple(segs[:3]))
