Triangle Numbers
================

Given a triangle of numbers where each number is equal to the sum of the three numbers on top of it, find the first even number in a row.

**Explanatory Note:** The vertex of the triangle (at the top) is 1. The structure of the triangle is shown below. Each number is equal to the sum of the numbers at the following positions: Position X: immediately above it. Position Y and Z: to the immediate left and right of X. In case there are no numbers at position X or Y or Z, assume that there is a zero (0) over there. This can occur for positions at the edge. 

Here are four rows of the triangle:

              1
          1   1  1
       1  2   3  2  1
    1  3  6   7  6  3  1

### Input and Constraints:

First line a number `1 <= T <= 100` (number of test cases).

T lines with a number `3 <= N <= 1000000000` (the row number, assuming that the top vertex of the triangle is Row 1).

### Output:

For each test case the position of the first even number, assuming the left most number in a row is Position 1.

If there is no even number in a row, print -1.

### Sample Input:

    2
    3
    4

### Sample Output:

    2
    3
