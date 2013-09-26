Lego Blocks
==========

You have 4 types of lego blocks, of sizes 1 * 1 * 1, 1 * 1 * 2, 1 * 1 * 3 and 1 * 1 * 4. Assume you have infinite number of blocks of each type.

You want to make a wall of height N and width M out of these blocks. The wall should not have any holes in it. The wall you build should be one solid structure. A solid structure means that it should not be possible to separate the wall along any vertical line without cutting any lego block used to build the wall. The blocks can only be placed horizontally. In how many ways can the wall be built?

### Input:

The first line contains the number of test cases T. T test cases follow. Each case contains two integers N and M.

### Output:

Output T lines, one for each test case containing the number of ways to build the wall. As the numbers can be very large, output the result modulo 1000000007.

### Constraints:

* 1 <= T <= 100
* 1 <= N,M <= 1000

### Sample Input:

    4
    2 2
    3 2
    2 3
    4 4

### Sample Output:

    3
    7
    9
    3375

### Explanation:

aa
bc

aa
bb

ab
cc

For the second case, each row of the wall can contain either two blocks of width 1, or one block of width 2. However, the wall where all rows contain two blocks of width 1 is not a solid one as it can be divided vertically. Thus the number of ways is 2 * 2 * 2 - 1 = 7.

PS:”aa” is one lego block of size 1 * 1 * 2, “b” and “c” are lego blocks of size 1 * 1 * 1.
