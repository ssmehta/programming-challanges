Sherlock and Watson
===================

John Watson performs an operation called *Right Circular Rotation* on an integer array a<sub>0</sub>, a<sub>1</sub>, ..., a<sub>n - 1</sub>. *Right Circular Rotation* transforms the array from a<sub>0</sub>, a<sub>1</sub>, ..., a<sub>n - 1</sub> to a<sub>N - 1</sub>, a<sub>0</sub>, ..., a<sub>n - 2</sub>.

He performs the operation *K* times and tests Sherlock’s ability to identify the element at a particular position in the array. He asks *Q* queries. Each query consists of one integer *x*, for which you have to print the element *a<sub>x</sub>*.

### Input:

The first line consists of 3 integers *N*, *K* and *Q* separated by a single space.

The next line contains *N* space separated integers which indicates the elements of the array *A*.

Each of the next *Q* lines contain one integer per line denoting *x*.

### Output:

For each query, print the value in the location in a newline.

### Constraints:

* 1 <= N <= 10<sup>5</sup>
* 1 <= A[i] <= 10<sup>5</sup>
* 1 <= K <= 10<sup>5</sup>
* 1 <= Q <= 500
* 0 <= x <= N - 1

### Sample Input:

    3 2 3
    1 2 3
    0
    1
    2

### Sample Output:

    2
    3
    1

### Explanation:

After one rotation array becomes, 3 1 2.

After another rotation array becomes 2 3 1. 

Final array now is 2,3,1. 0th element of array is 2. 

1st element of array is 3.

2nd element of array is 1.