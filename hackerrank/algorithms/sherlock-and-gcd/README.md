Sherlock and GCD
================

Sherlock is stuck. He has an array *A<sub>1</sub>*, *A<sub>2</sub>*, ..., *A<sub>N</sub>*. He wants to know if there exists a subset, *B* = {*A<sub>i1</sub>*, *A<sub>i2</sub>*, ..., *A<sub>ik</sub>*} where 1 <= *i1* < *i2* < ... < *ik* <= *N*, of this array which follows the property

* *B* is non-empty subset.
* There exists no integer *x* (*x* > 1) which divides all elements of *B*. Note that *x* may or may not be an element of *A*.

### Input:

First line contains *T*, the number of testcases. Each testcase consists of *N* in one line. The next line contains *N* integers denoting the array *A*.

### Output:

Print `YES` or `NO`, if there exists any such subset or not, respectively.

### Constraints:

* 1 <= *T* <= 10
* 1 <= *N* <= 100
* 1 <= *A<sub>i</sub>* <= 10<sup>5</sup> ∀ 1 <= *i* <= *N*

### Sample Input:

    2
    3
    1 2 3
    2
    2 4

### Sample Output:

    YES
    NO

### Explanation:

In first testcase, *S* = {1}, *S* = {1, 2}, *S* = {1,3}, S = {2, 3} and S = {1, 2, 3} are all the possible subsets which satisfy the given condition.  
In second testcase, no non-empty subset exists which satisfies the given condition.