Basic Statistics Warmup
=======================

You are given an array of N integers separated by spaces, all in one line.

Display the following:

1. Mean (m): The average of all the integers.

2. Median: In case, the number of integers is odd, the middle element; else, the average of the middle two elements.

3. Mode: The element(s) which occurs most frequently. If multiple elements satisfy this criteria, display the numerically smallest one.

4. Standard Deviation (SD).

    SD = (((x<sub>1</sub>-m)<sup>2</sup>+(x<sub>2</sub>-m)<sup>2</sup>+(x<sub>3</sub>-m)<sup>2</sup>+(x<sub>4</sub>-m)<sup>2</sup>+…(x<sub>N</suba>-m)<sup>2</sup>))/N)<sup>0.5</sup>

    where x<sub>i</sub> is the ith element of the array

5. Lower and Upper Boundary of the 95% Confidence Interval, separated by a space. This might be a new term to some. However, it is an important concept with a simple, formulaic solution. Look it up!

Other than the modal values (which should all be integers) the answers should be in decimal form till one place of decimal (0.0 format). An error margin of +/- 0.1 will be tolerated for the standard deviation and the confidence interval boundaries. The mean, mode and median values should match the expected answers exactly.

### Input:

The first line contains the number of integers.
The second line contains space separated integers for which you need to find the mean, median, mode, standard deviation and confidence interval boundaries.

### Constraints:

* 10 <= N <= 2500
* 0 < xi <= 105

### Output:

A total of five lines are required.

    Mean (format:0.0) on the first line
    Median (format: 0.0) on the second line
    Mode(s) (Numerically smallest Integer in case of multiple integers)
    Standard Deviation (format:0.0) 
    Lower and Upper Boundary of Confidence Interval (format: 0.0) with a space between them.

### Sample Input:

    10
    64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

### Sample Output:

    43900.6
    44627.5
    4978
    30466.9
    25017.0 62784.2

### Scoring:

Scoring is proportional to the number of test cases cleared.
