Sherlock and Planes
===================

Watson gives four 3-dimensional points to Sherlock and asks him if they all lie in the same plane. Your task here is to help Sherlock.

### Input:

First line contains *T*, the number of testcases.

Each test case consists of four lines. Each line contains three integers, denoting *x<sub>i</sub>* *y<sub>i</sub>* *z<sub>i</sub>*.

### Output:

For each test case, print `YES` or `NO` whether all four points lie in same plane or not, respectively.

### Constraints:

* 1 <= *T* <= 10<sup>4</sup>
* -10<sup>3</sup> <= *x<sub>i</sub>*, *y<sub>i</sub>*, *z<sub>i</sub>* <= 10<sup>3</sup>

### Sample Input:

	1
	1 2 0
	2 3 0
	4 0 0
	0 0 0

### Sample Output:

	YES

### Explanation:

All points have *z<sub>i</sub> = 0*, hence they lie in the same plane, and output is `YES`.
