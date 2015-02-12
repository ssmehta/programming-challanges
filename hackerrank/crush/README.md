Algorithmic Crush
=================

Devendra is on cloud nine after seeing his crush smiling at him in class. At that very moment his professor singles him out and asks him a question. Devendra’s mind is all too fuzzy with his crush and her smile to concentrate on anything else. Help him solve the problem:

You are given a list of size *N*, initialized with zeroes. You have to perform *M* queries on the list and output the maximum of final values of all the *N* elements in the list. For every query, you are given three integers *a*, *b* and *k* and you have to add value *k* to all the elements ranging from index a to b(both inclusive).

### Input:

First line will contain two integers *N* and *M* separated by a single space.

Next M lines will contain three integers *a*, *b* and *k* separated by a single space.

Numbers in list are numbered from 1 to *N*.

### Output:

A single line containing *maximum value in the final list*.

### Constraints:

* 3 <= *N* <= 10<sup>7</sup>
* 1 <= *M* <= 2 * 10<sup>5</sup>
* 1 <= *a* <= *b* <= *N*
* 0 <= *k* <= 10<sup>9</sup>

### Sample Input:

	5 3
	1 2 100
	2 5 100
	3 4 100

### Sample Output:

	200

### Explanation:

After first update list will be `100 100 0 0 0`. 

After second update list will be `100 200 100 100 100`.

After third update list will be `100 200 200 200 100`.

So the required answer will be 200.