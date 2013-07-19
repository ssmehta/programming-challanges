Journey to Mars
===============

Elon Musk has succesfully built a staircase from Earth to Mars. There is an automated machine which will take anyone to Mars using the stairs. A lot of people would want to go Mars, which is not possible due to limited capacity of the automated machine. Hence, Elon asks interested candidates to solve an interesting challenge, based on which they will be chosen.

Sam is highly interested in going to Mars. Can you help him solve the challenge? 

Suppose there are N steps in the staircase which is connecting Earth and Mars, the automated machine can go step by step or at each step, it can take a jump of utmost N steps.

Elon is interested to know the number of ways in which you can go to Mars.

Since the number of steps in stairs can be insanely large, Elon is only interested in the first and the last K digits of number of ways from which he can compute the actual answer with his algorithm. 

### Input Format:

First line is an integer T which is the number of test cases.

Next T lines contains 2 integers N and K.

### Output Format:

T lines. Each line will correspond to one of the test cases containing the sum of numbers which are formed by first K digit and last K digits of number of ways.

### Constraints:

* 1 <= T <= 1000
* 1 <= N <= 10^9
* 1 <= K <= 9

If S is the number of ways in which one can climb the staircase, then the number of digits in S is greater or equal to the K.

### Sample Input:

    2
    10 2
    12 1

### Sample Output:

    63
    10

### Explanation:

If there are 10 steps, let’s call the number of ways in which one can go is S.

let S be of the form wxyz.

So, summing wx + yz given 63.
