Sherlock and Counting
=====================

Watson gives Sherlock two integers **N** and **K** and asks him to count the number of positive integers **i** such that

**i * (N - i) <= N * K and i < N.**

### Input:

First line contains, **T**, the number of testcases. Each testcase consists of N and K in one line.

### Output:

For each testcase, print in one line the required answer.

### Constraints:

* 1 <= **T** <= 10<sup>5</sup>
* 1 <= **N**, **K** <= 10<sup>9</sup>

### Sample Input:

    2
    5 1
    5 2

### Sample Output:

    2
    4

### Explanation:

Testcase 1: **i** = 1, 4 satisfy.

Testcase 2: **i** = 1, 2, 3, 4 satisfy.
