Special Multiple
================

You are given an integer *N*. Can you find the least positive integer *X* made up of only 9’s and 0’s such that *X* is a multiple of *N*?  *X* is made up of one or more occurences of 9 and zero or more occurences of 0.

### Input:

The first line contains an integer T which denotes the number of test cases. T lines follow.

Each line contains the integer *N* for which the solution has to be found.

### Output:

Print the answer *X* to STDOUT corresponding to each test case. The output should not contain any leading zeroes.

### Constraints:

* 1 <= T <= 10<sup>4</sup>
* 1 <= N <= 500

### Sample Input:

    3
    5
    7
    1

### Sample Output:

    90
    9009
    9

### Explanation:

90 is the smallest number made up of 9’s and 0’s divisible by 5. You can derive similarly for other cases.
