#!/usr/bin/env python

import itertools, sys


class Point:
    def __init__(self, x, y, v):
        self.x, self.y, self.v = x, y, v
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    points = [Point(*list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
    

    # Max weight - update compares max_weight to the smaller total weight
    max_weight = 0
    best_weight = lambda a, b: max(max_weight, min(a, b))
    
    # Determinant of:
    #     | (b.x - a.x) (c.x - a.x) |
    #     | (b.y - a.y) (c.y - a.y) |
    # where a and b are points defining the line, and c is the test point
    det = lambda a, b, c: (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    
    
    for a, b in itertools.combinations(points, 2):
        above, below = 0, 0
        
        for c in (p for p in points if p != a and p != b):
            if det(a, b, c) > 0:
                above += c.v
            else:
                below += c.v
        
        max_weight = best_weight(above + a.v + b.v, below)
        max_weight = best_weight(above + a.v, below + b.v)
        max_weight = best_weight(above + b.v, below + a.v)
        max_weight = best_weight(above, below + a.v + b.v)
    
    print(max_weight)