Help Mike
=========

Harvey Specter has agreed to take Mike Ross to a meeting with NSA filled with brilliant scientists. But, as always, its not going to be easy for Mike. He has to solve a puzzle given by Harvey.

Harvey gives two numbers N and K and defines a set A.

*A = {x : x is a natural number <= N}*
(i.e), A = {1, 2, 3, 4, 5, 6, ..., N}

Mike has to find the total number of pairs of elements A[i] and A[j] belonging to the given set such that i < j and their sum is divisible by K.

### Input:

An integer T followed by T lines, each containing a pair of integers N and K separated by a single space.

### Output:

T integers on separate lines each corresponding to the answer to that test case.

### Constraints:

* 1 <= T <= 100
* 1 <= N <= 10<sup>9</sup>
* 1 <= K <= 10000

### Sample Input:

    2
    10 4
    7 3

### Sample Output:

    10
    7

### Explanation:

For the 1st test case, there are 10 pairs whose sum is divisible by 4. 
(1,3), (1,7), (2,6), (2,10), (3,5), (3,9), (4,8), (5,7), (6,10) and (7,9)

For the 2nd test case, there are 7 pairs whose sum is divisible by 3. 
(1,2), (1,5), (2,4), (2,7), (3,6), (4,5) and (5,7)
