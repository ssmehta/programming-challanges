#!/usr/bin/env python

"""
Problem 102:

Three distinct points are plotted at random on a Cartesian plane, for which
-1000 <= x, y <= 1000, such that a triangle is formed.

Consider the following two triangles:

        A(-340,495), B(-153,-910), C(835,-947)

        X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ
does not.

Using triangles.txt, a 27K text file containing the co-ordinates of one thousand
"random" triangles, find the number of triangles for which the interior contains
the origin.

NOTE: The first two examples in the file represent the triangles in the example
given above.
"""


area = lambda A, B, C: abs(A[0]*B[1] - A[0]*C[1] + B[0]*C[1] - B[0]*A[1] + C[0]*A[1] - C[0]*B[1])
data = [list(map(int, s.split(','))) for s in open('problem102-triangles.txt')]

n = 0

for x in data:
    A, B, C, X = (x[0], x[1]), (x[2], x[3]), (x[4], x[5]), (0, 0)
    
    if area(A, B, C) == area(A, B, X) + area(A, X, C) + area(X, B, C):
        n += 1

print(n)
