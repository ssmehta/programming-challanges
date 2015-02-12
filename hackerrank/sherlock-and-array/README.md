Sherlock and Array
==================

Watson gives Sherlock an array *A<sub>1</sub>*, *A<sub>2</sub>*, ..., *A<sub>N</sub>*.  Then he asks him to find if there exists an element in the array, such that, the sum of elementson its left is equal to the sum of elements on its right.  If there are no elements to the left/right, then the sum is considered to be zero.  Formally, find an *i*, such that, *A<sub>1</sub>* + *A<sub>2</sub>* + ... + *A<sub>i - 1</sub>* = *A<sub>i + 1</sub>* + *A<sub>i + 1</sub>* + ... + *A<sub>N</sub>*.

### Input:

First line contains, *T*, the number of test cases.  For each test case, the first line contains *N*, the number of elements in the array *A*.  The second line for each test case contains *N* space separated integers, denoting the array *A*.  

### Output:

For each test case, `YES` if there exists an element in the array, such that, the sum of elements on its left equal to the sum of elements on its right, else print `NO`.

### Constraints:

* 1 <= *T* <= 10
* 1 <= *N* <= 10<sup>5</sup>
* 1 <= *A<sub>i</sub>* <= 2 * 10<sup>4</sup> for 1 <= *i* <= N

### Sample Input:

    2
    3
    1 2 3
    4
    1 2 3 3

### Sample Output:

    NO
    YES

### Explanation:

For test case 1, no such index exists

For test case 2, *A<sub>1</sub>* + *A<sub>2</sub>* = *A<sub>4</sub>*, therefore index 3 satisfies