Binomial Coefficients
=====================

In mathematics, binomial coefficients are a family of positive integers that occur as coefficients in the binomial theorem. nCk denotes the number of ways of choosing k objects from n different objects.

However when n and k are too large, we often save them after modulo operation by a prime number P. Please calculate how many binomial coefficients of n become to 0 after modulo by P.

### Input:

The first of input is an integer T, the number of test cases.

Each of the following T lines contains 2 integers, n and prime P.

### Output:

For each test case, output a line contains the number of nCk's (0 <= k <= n) each of which after modulo operation by P is 0.

### Sample Input:

    3
    2 2
    3 2
    4 3

### Sample Output:

    1
    0
    1

### Constraints:

* T is less than 100.
* n is less than 10<sup>500</sup>.
* P is less than 10<sup>9</sup>.
