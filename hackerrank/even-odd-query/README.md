Even Odd Query
==============

You are given an array *A* of size *N*. You are also given an interger *Q*. Can you figure out the answer to each of the *Q* queries?

Each query contains 2 integers *x* and *y*, and you need to find whether the value find(x, y) is Odd or Even:

	find(int x, int y) {
		if(x > y) return 1;
		ans = pow(A[x], find(x + 1, y))
		return ans
	}

Note: pow(a, b) = *a*<sup>*b*</sup>.

### Input:

The first line of the input contains an integer *N*. The next line contains N space separated non-negative integers (whole numbers less than or equal to 9).

The line after that contains a positive integer, *Q*, the denotes the number of queries to follow. *Q* lines follow, each line contains two positive integer *x* and *y* separated by a single space.

### Output:

For each query, display 'Even' if the value returned is Even, otherwise display 'Odd'.

### Constraints:

* 2 <= *N* <= 10<sup>5</sup>
* 2 <= *M* <= 10<sup>5</sup>
* 1 <= *x*, *y* <= *N*
* *x* <= *y*

### Sample Input:

	3
	3 2 7
	2
	1 2
	2 3

### Sample Output:

	Odd
	Even

### Explanation:

find(1, 2) = 9, which is Odd  
find(2, 3) = 128, which is Even