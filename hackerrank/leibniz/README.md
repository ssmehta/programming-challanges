Lonely Integer
==============

In Calculus, the [Leibniz formula for π](http://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) is given by:

![Leibniz](https://s3.amazonaws.com/hr-filepicker/Leibnitz+infinite+series.png)

or:

![Summation](https://s3.amazonaws.com/hr-filepicker/Leibniz+pi+summation.png)

You will be given an integer ‘n’. Your task is to print the summation of the Leibniz formula up to the n<sup>th</sup> term of the series correct to 15 decimal places.

### Input:

The first line contains an integer T (<= 100). T testcases follow. Each testcase has a single line with a positive integer n (< 10<sup>7</sup>).

### Output:

Output T lines, with each line containing the summation up to nth term.

![Summation](https://s3.amazonaws.com/hr-filepicker/Leibniz+ith+sum.png)

### Sample Input:

    2
    10
    20

### Sample Output:

    0.760459904732351
    0.772905951666960


### Scoring:

This is a code golf question, the goal is to write a solution with as little code as possible. A correct submission with a source code of X characters will receive the following score:

maxScore * (300 - X) / 300

Any correct code longer than 300 characters will receive a score of maxScore * 0.001.
MaxScore is the maximum score attainable for the problem.
