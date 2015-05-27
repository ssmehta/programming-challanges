Filling Jars
============

Sunny and Johnny together have M dollars which they intend to use at the ice cream parlour. Among N flavors available, they have to choose two distinct flavors whose cost equals M. Given a list of cost of N flavors, output the indices of two items whose sum equals M. The cost of a flavor (c<sub>i</sub>) will be no more than 10000.

### Input:

The first line of the input contains T, T test cases follow. 

Each test case follows the format: The first line contains M. The second line contains the number N. The third line contains N single space separated integers denoting the price of each flavor c<sub>i</sub>.

### Output:

Output two integers, each of which is a valid index of the flavor. The lower index must be printed first. Indices are indexed from 1 to N.

### Constraints:

* 1 <= T <= 50
* 2 <= M <= 10000
* 2 <= N <= 10000
* 1 <= c<sub>i</sub> <= 10000

The prices of two items may be same and each test case has a unique solution.

### Sample Input:

    2
    4
    5
    1 4 5 3 2
    4
    4
    2 2 4 3

### Sample Output:

    1 4
    1 2

### Explanation:

The sample input has two test cases. For the 1st, the amount M = 4 and there are 5 flavors at the store. The flavors indexed at 1 and 4 sums to 4. For the 2nd test case, the amount M = 4 and the flavors indexed at 1 and 2 sums to 4.
