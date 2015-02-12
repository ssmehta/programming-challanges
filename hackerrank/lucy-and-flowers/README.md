Lucy and Flowers
================

Little Lucy loves to arrange her flowers in patterns similar to those of a binary search tree. Her father, a computer scientist himself, takes note of this and finds out that she has *N* flowers. Every day she takes some of these *N* flowers and arranges them into all possible different patterns. The more the number of arrangements, the more time she spends outside.

Now, her father knows that she takes a non-empty subset of these *N* flowers any given day. He wants to find out the total number of arrangements that she can ever make. As this may be too large to handle, you only need to report final answer modulo 10<sup>9</sup> + 9 if the answer is no less than 10<sup>9</sup> + 9.

**Note**: All flowers are distinct and are labelled by distinct numbers.

### Input:

The first line contains an integer, *T*, the number of test cases.

The next *T* lines contain a single integer each and denote the labels of the respective *N* flowers.

### Output:

A single line containing *maximum value in the final list*.

### Constraints:

* 1 <= *T* <= 5000
* 1 <= *N* <= 5000

### Sample Input:

	4
	1
	2
	3
	4

### Sample Output:

	1
	4
	14
	50

### Explanation:

For the first case, only one BST is possible.

For the second case, only 4 BSTs are possible (shown below).

	1    2    1      2
	           \    / 
	            2   1

Similarly, 14 BSTs are possible for N = 3, and 50 are possible for N = 4.
