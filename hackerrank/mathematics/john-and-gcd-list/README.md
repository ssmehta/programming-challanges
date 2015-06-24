John and GCD List
=================

John is new to Mathematics and does not know how to calculate GCD of numbers. So he wants you to help him in a few GCD calculations. John has a list *A* of numbers, indexed 1 to *N*. He wants to create another list *B* having *N* + 1 numbers, indexed from 1 to *N* + 1, and having the following property:

    GCD(B[i], B[i+1]) = A[i], ∀ 1 <= i <= N

As there can be many such lists, John wants to know the list *B* in which sum of all elements is minimum. It is guaranteed that such a list will always exist.

### Input:

First line will contain an integer *T* representing the number of test cases Each test case will contain a string having length (*a* + *b*) which will be concatenation of both the strings described in problem. The string will only contain small letters and without any spaces.

### Output:

For each test case, print in a new line the list *B* such that each element is separated by a single space.


### Constraints:

* 1 <= *T* <= 10
* 2 <= *N* <= 10<sup>3</sup> 
* 1 <= *A[i]* <= 10<sup>4</sup> 
* 1 <= *B[i]*

### Sample Input:

    2
    3
    1 2 3
    3
    5 10 5

### Sample Output:

    1 2 6 3
    5 10 10 5

### Explanation:

For the first testcase,

    GCD(1,2) = 1
    GCD(2,6) = 2
    GCD(6,3) = 3
    sum = 1+2+6+3 = 12 which is minimum among all possible list B

For the second testcase,

    GCD(5, 10) = 5
    GCD(10, 10) = 10
    GCD(10, 5) = 5
    sum = 5 + 10 + 10 + 5 = 30 which is the minimum among all possible list B