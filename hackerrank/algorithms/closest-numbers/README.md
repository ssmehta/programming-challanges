Closest Numbers
===============

Sorting is often useful as the first step in many different tasks. The most common task may to be make things easier to find later, but there are other uses also.

### Challenge:

Given a list of unsorted numbers, can you find the numbers that have the smallest absolute difference between them? If there are multiple pairs, find them all.

### Input:

There will be two lines of input:

* *n* - the size of the list
* *array* - the *n* numbers of the list

### Output:

Output the pairs of numbers with the smallest difference. If there are multiple pairs, output all of them in ascending order, all on the same line (consecutively) with just a single space between each pair of numbers. If there’s a number which lies in two pair, print it two times (see sample case #3 for explanation).

### Constraints:

* 10 <= n <= 200000
* -10<sup>7</sup> <= x <= 10<sup>7</sup>, x ∈ array
* array[i] != array[j], 0 <= i, j < N and i != j

### Sample Input #00:

    10
    -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854

### Sample Output #00:
    
    -20 30

### Explanation #00:

30 - (-20) = 50, which is the smallest difference.

### Sample Input #01:

    12
    -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470

### Sample Output #01:
    
    -520 -470 -20 30

### Explanation #01:

(-470) - (-520) = 30 - (-20) = 50, which is the smallest difference.

### Sample Input #02:

    4
    5 4 3 2

### Sample Output #02:
    
    2 3 3 4 4 5

### Explanation #02:

Here minimum difference will be 1. So valid pairs (2, 3), (3, 4), (4, 5). So we have to print 2 one time, 3 and 4 two times and 5 one time.