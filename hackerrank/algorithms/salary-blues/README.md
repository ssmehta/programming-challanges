Salary Blues
============

Manager of HackerX company is having big trouble. Workers are very unhappy with the way salary is provided to them. They want every worker to have the same salary, otherwise they will go on strike.

Their current salaries are denoted by sequence of **N** integers **A<sub>1</sub>**, **A<sub>2</sub>**, **A<sub>3</sub>**, ..., **A<sub>N</sub>** . Manager has decided to take action and make their salaries equal. He uses the following process until all salaries are equal. This method is called as normalization:

1.  Select any two different values from **A**.

2.  Replace larger value with the difference of the two. Difference of two positive integers **B** and **C** is defined as **|B - C|**.

He knows that the final value will always be unique.
Now, **Q** queries are given. In each query you are given integer **K**.  **K** is the amount to be added to everyone’s salary as bonus, before the normalization.

### Input:

First line contains, **N** and **Q**, the number of employees and the number of queries. Next line contains **N** space separated positive integers denoting the array **A**. Next **Q** lines contain queries. Each query consists of one integer per line denoting **K**.

### Output:

For each query, print the normalized salary (which is same for everyone in the end) in one line.

### Constraints:

* 1 <= N <= 10<sup>5</sup>
* 1 <= Q <= 10<sup>5</sup>
* 1 <= A[i] <= 10<sup>14</sup>
* 0 <= K <=10<sup>9</sup>

### Sample Input:

    4 2
    9 12 3 6
    0
    3

### Sample Output:

    3
    3

### Explanation:

If 0 is added to every element of array A, it will remain same.

One way to normalize A is this:

1. Picking 12 and 3 gives: 9 9 3 6
2. Picking 3 and 6 gives: 9 9 3 3
3. Picking 9 and 3 gives: 6 9 3 3
4. Picking 9 and 3 gives: 6 6 3 3
5. Picking 6 and 3 gives: 3 6 3 3
6. Picking 6 and 3 gives: 3 3 3 3
