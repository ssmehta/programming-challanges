Grid Walking
============

You are situated in an N dimensional grid at position(x_1, x_2, ..., x_N). The dimensions of the grid are (D_1, D_2, ..., D_N). In one step, you can walk one step ahead or behind in any one of the N dimensions. (So there are always 2N possible different moves). In how many ways can you take M steps such that you do not leave the grid at any point ? You leave the grid if you for any x_i, either x_i <= 0 or x_i > D_i.

### Input:

The first line contains the number of test cases T. T test cases follow. For each test case, the first line contains N and M, the second line contains x_1, x_2, ..., x_N and the 3rd line contains D_1,D_2,…,D_N.

### Output:

Output T lines, one corresponding to each test case. Since the answer can be really huge, output it modulo 1000000007.

### Constraints:

* 1 <= T <= 10
* 1 <= N <= 10
* 1 <= M <= 300
* 1 <= D_i <= 100
* 1 <= x_i <= D_i

### Sample Input:

    10
    1 287
    44
    78
    1 236
    25
    87
    1 122
    41
    63
    1 260
    7
    64
    1 127
    3
    73
    1 69
    6
    68
    1 231
    14
    63
    1 236
    13
    30
    1 259
    38
    70
    1 257
    11
    12

### Sample Output:

    38753340
    587915072
    644474045
    423479916
    320130104
    792930663
    846814121
    385120933
    60306396
    306773532
