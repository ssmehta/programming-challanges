#!/usr/bin/env python

import bisect, sys


def interpolate(x0, y0, x1, y1, x):
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    
if __name__ == '__main__':
    t = float(sys.stdin.readline())
    x, y = [], []
    
    # Load training set
    with open('trainingdata.txt', 'r') as f:
        for line in f:
            line = tuple(map(float, line.split(',')))
            
            if line[0] not in x:
                idx = bisect.bisect_left(x, line[0])
                x.insert(idx, line[0])
                y.insert(idx, line[1])
    
    # Perform interpolation
    idx = bisect.bisect_left(x, t)
    
    if idx > 0:
        print(interpolate(x[idx - 1], y[idx - 1], x[idx], y[idx], t))
    else:
        print(interpolate(x[idx], y[idx], x[idx + 1], y[idx + 1], t))
