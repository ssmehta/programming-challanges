Stock Maximize
==============

Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next N days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

### Input:

The first line contains the number of test cases T. T test cases follow:

The first line of each test case contains a number N. The next line contains N integers, denoting the predicted price of WOT shares for the next N days.

### Output:

Output T lines, containing the maximum profit which can be obtained for the corresponding test case.

### Constraints:

* 1 <= T <= 10
* 1 <= N <= 50000

All share prices are between 1 and 100000

### Sample Input:

    3
    3
    5 3 2
    3
    1 2 100
    4
    1 3 1 2

### Sample Output:

    0
    197
    3
