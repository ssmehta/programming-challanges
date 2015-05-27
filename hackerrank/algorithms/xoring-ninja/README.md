Xoring Ninja
============

Given a list containing N integers, calculate the XOR_SUM of all the non-empty subsets of the list and print the value of sum % (10<sup>9</sup> + 7).

XOR operation on a list (or a subset of the list) is defined as the XOR of all the elements present in it. 

E.g. XOR of list containing elements `{A, B, C} = ((A ^ B) ^ C)`, where `^` represents XOR.

E.g. XOR_SUM of list A having three elements `{X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>}` can be given as follows.  All non-empty subsets will be {X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>, (X<sub>1</sub>, X<sub>2</sub>), (X<sub>2</sub>, X<sub>3</sub>), (X<sub>1</sub>, X<sub>3</sub>), (X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>)}`.

XOR_SUM(A) = X<sub>1</sub> + X<sub>2</sub> + X<sub>3</sub> + X<sub>1</sub> ^ X<sub>2</sub> + X<sub>2</sub> ^ X<sub>3</sub> + X<sub>1</sub> ^ X<sub>3</sub> + ((X<sub>1</sub> ^ X<sub>2</sub>) ^ X<sub>3</sub>)

### Input:

An integer T, denoting the number of testcases. 2T lines follow.

Each testcase contains two lines, first line will contains an integer N followed by second line containing N integers separated by a single space.

### Output:

T lines, i<sup>th</sup> line containing the output of the i<sup>th</sup> testcase.

### Constraints:

* 1 <= T <= 5
* 1 <= N <= 10<sup>5</sup>
* 1 <= A[i] <= 10<sup>9</sup>

### Sample Input:

    1
    3
    1 2 3

### Sample Output:

    12

### Explanation:

The given case will have 7 non-empty subsets whose XOR is given below

	1 = 1
	2 = 2
	3 = 3
	1 ^ 2 = 3
	2 ^ 3 = 1
	3 ^ 1 = 2
	1 ^ 2 ^ 3 = 0

So sum of all such XORs is 12.
