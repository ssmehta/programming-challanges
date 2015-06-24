#!/usr/bin/env python

import sys


if __name__ == '__main__':
    S = sys.stdin.readline().strip()
    
    PM = S.endswith('PM')
    H, M, S = list(map(int, S[:-2].split(':')))
    
    if H == 12 and not PM:
        print('%02d:%02d:%02d' % (0, M, S))
    elif H < 12 and PM:
        print('%02d:%02d:%02d' % (H + 12, M, S))
    else:
        print('%02d:%02d:%02d' % (H, M, S))