K Candy Store
=============

Jim enters a candy shop which has N different types of candies, each candy is of the same price. Jim has enough money to buy K candies. In how many different ways can he purchase K candies if there are infinite candies of each kind?

### Input:

The first line contains an integer T, the number of tests.

This is followed by 2T lines which contain T tests:

The first line (of each testcase) is an integer N and the second line (of each testcase) is an integer K.

### Output:

For each testcase, print the number of ways Jim can buy candies from the shop in a newline. If the answer has more than 9 digits, print the last 9 digits.

### Note:

This problem may expect you to have solved [nCr Table](https://www.hackerrank.com/challenges/ncr-table).

### Constraints:

* 1 <= T <= 200
* 1 <= N < 1000
* 1 <= K < 1000

### Sample Input:

    2
    4
    1
    2
    3

### Sample Output:

    4
    4

### Explanation:

There are 2 testcases, for the first testcase we have N = 4 and K = 1, as Jim can buy only 1 candy, he can choose to buy any of the 4 types of candies available. Hence, his answer is 4. For the 2nd testcase, we have N = 2 and K = 3, If we name two chocolates as **a** and **b**, he can buy

    aaa bbb aab abb

chocolates, hence 4.
