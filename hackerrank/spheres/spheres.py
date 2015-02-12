#!/usr/bin/env python

import math, sys



if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    mag = lambda p: math.sqrt(sum(x * x for x in p))
    dist = lambda p1, p2: mag(y - x for x, y in zip(p1, p2))
    
    for _ in range(T):
        R1, R2 = list(map(int, sys.stdin.readline().split()))
        p1 = list(map(int, sys.stdin.readline().split()))
        a1 = list(map(int, sys.stdin.readline().split()))
        p2 = list(map(int, sys.stdin.readline().split()))
        a2 = list(map(int, sys.stdin.readline().split()))
        
        dp = [y - x for x, y in zip(p1, p2)]
        da = [y - x for x, y in zip(a1, a2)]

        t2 = -2.0 * sum(p * a for p, a in zip(dp, da)) / sum(a * a for a in da)
        
        if t2 >= 0:
            print('YES' if mag(p + a * t2 / 2 for p, a in zip(dp, da)) <= R1 + R2 else 'NO')
        else:
            print('NO')