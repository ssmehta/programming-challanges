Lonely Integer
==============

There are N integers in an array *A*. All but one integer occurs in pairs. Your task is to find out that number that occurs only once.

### Input:

The first line of the input contains an integer *N* indicating number of integers in the array *A*.

Next line contains *N* integers each separated by a single space.

### Constraints:

* 1 <= N < 100
* N % 2 = 1 (N is an odd number)
* 0 <= A[i] < 100, ∀ i ∈ [1, N]

### Output:

Output (S) which is the number that occurs only once.

### Sample Input #00:

    1
    1

### Sample Output # 00:

    1

### Sample Input #01:

    3
    1 1 2

### Sample Output # 01:

    2

### Sample Input #02:

    5
    0 0 1 2 1

### Sample Output # 02:

    2

### Explanation:

In the first input, we see only 1 element and that element is the answer (1).

In the second input, we see 3 elements, 1 is repeated twice, the only other element 2 is the answer.

In the third input, we see 5 elements, 1 and 0 are repeated twice, the other element 2 is the answer.
