#!/usr/bin/python

import collections, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    x = sorted(map(int, sys.stdin.readline().split()))
    
    
    # Mean
    mean = 1.0 * sum(x) / len(x)
    print('%.1f' % mean)
    
    
    # Median
    mid = len(x) // 2
    
    if len(x) % 2:
        print('%.1f' % x[mid])
    else:
        print('%.1f' % ((x[mid - 1] + x[mid]) / 2.0))
    
    
    # Mode
    c = collections.Counter(x)
    mode, freq = max(x), max(c.values())
    
    for k in c:
        if c[k] == freq and k < mode:
            mode = k
    
    print(mode)
    
    
    # Standard Deviation
    std = (1.0 * sum((n - mean) * (n - mean) for n in x) / N)**0.5
    print('%.1f' % std)
    
    
    # Confidence Interval
    error = 1.96 * std / N**0.5
    print('%.1f %.1f' % (mean - error, mean + error))
    
