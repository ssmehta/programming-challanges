Closest Number
==============

You are given 3 numbers *a*, *b* and *x*. You need to output the multiple of *x* which is closest to *a<sup>b</sup>*. If more than one answer exists, display the smallest one.

### Input:

The first line contains *T*, the number of test cases.  
*T* lines follow, each line contains 3 space separated integers (*a*, *b* and *x* respectively).

### Output:

For each test case , output the multiple of *x* which is closest to *a<sup>b</sup>*

### Constraints:

* 1 <= *T* <= 10<sup>5</sup>
* 1 <= *x* <= 10<sup>9</sup>
* 0 < *a<sup>b</sup>* <= 10<sup>9</sup>
* 1 <= *a* <= 10<sup>9</sup>
* -10<sup>9</sup> <= *b* <= 10<sup>9</sup>

### Sample Input:

	3
	349 1 4
	395 1 7
	4 -2 2

### Sample Output:

	348
	392
	0

### Explanation:

The closest multiple of 4 to 349 is 348.  
The closest multiple of 7 to 395 is 392.  
The closest multiple of 2 to 1/16 is 0.