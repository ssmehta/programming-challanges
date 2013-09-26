#!/usr/bin/env python

"""
Point in Circle

Challenge Description:

Having coordinates of the center of a circle, it's radius and coordinates of a point you need to define whether this point is located inside of this circle.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)
    Center: (5.05, -11); Radius: 21.2; Point: (-31, -45)
    Center: (-9.86, 1.95); Radius: 47.28; Point: (6.03, -6.42)

All numbers in input are between -100 and 100

Output sample:

Print results in the following way.

    true
    false
    true
"""

import re, sys


if __name__ == '__main__':
    regex = re.compile(r'(-?\d+(\.\d+)?)')
    
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                cx, cy, r, px, py = [float(x[0]) for x in regex.findall(line)]
                
                if (cx - px)**2 + (cy - py)**2 > r * r:
                    print('false')
                else:
                    print('true')
