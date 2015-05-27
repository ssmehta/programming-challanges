Insertion Sort Advanced Analysis
================================

Insertion Sort is a simple sorting technique which was covered in previous challenges. In the running time challenge, we directly counted how many shifts (or swaps) it takes for insertion sort to finish sorting an array. However, some arrays may be too large for us to wait around for insertion sort to finish. Is there some other way we can calculate the number of times Insertion Sort shifts over elements when sorting an array?

### Input:

The first line contains the number of test cases T. T test cases follow. The first line for each case contains N, the number of elements to be sorted. The next line contains N integers a[1],a[2]…,a[N].

### Output:

Output T lines, containing the required answer for each test case.

### Constraints:

* 1 <= T <= 5
* 1 <= N <= 100000
* 1 <= a[i] <= 1000000

### Sample Input:

    2
    5
    1 1 1 2 2
    5
    2 1 3 1 2

### Sample Output:

    0
    4
