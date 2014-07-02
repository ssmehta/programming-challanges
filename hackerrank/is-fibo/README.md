Is Fibo
=======

You are given an integer N, can you check if the number is an element of fibonacci series? The first few elements of fibonacci series are 0, 1, 1, 2, 3, 5, 8, 13... A fibonacci series is one where every element is a sum of the previous two elements in the series. The first two elements are 0 and 1.

Formally:

* *fib<sub>0</sub> = 0*
* *fib<sub>1</sub> = 1*
* *fib<sub>n</sub> = fib<sub>n - 1</sub> + fib<sub>n - 2</sub>* ∀ n > 1

### Input:

First line contains T, number of test cases. 
T lines follows. Each line will contain an integer N.

### Output:

Output “IsFibo” (without quotes) if N is a fibonacci number and “IsNotFibo” (without quotes) if it is not a fibonacci number, in a new line corresponding to each test case.

### Constraints:

* 1 <= T <= 10<sup>5</sup>
* 1 <= N <= 10<sup>10</sup>

### Sample Input:

    3
    5
    7
    8

### Sample Output:

    IsFibo
    IsNotFibo
    IsFibo

### Explanation:

5 is a Fibonacci number given by *fib<sub>5</sub>* = 3 + 2
7 is not a Fibonacci number
8 is a Fibonacci number given by *fib<sub>6</sub>* = 5 + 3
