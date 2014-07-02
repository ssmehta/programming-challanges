Halloween Party
===============

Alex is attending a Halloween party with his girlfriend Silvia. At the party, Silvia spots a giant chocolate bar. If the chocolate can be served as only 1 x 1 sized pieces and Alex can cut the chocolate bar exactly *K* times, what is the maximum number of chocolate pieces Alex can cut and give Silvia?

### Input:

The first line contains an integer T denoting the number of testcases. T lines follow.

Each line contains an integer K.

### Output:

T lines. Each containing the output corresponding to the testcase.

### Constraints:

* 1 <= T <= 10
* 1 <= K <= 10<sup>7</sup>

**Note**

Chocolate needed to be served in size of 1 x 1 size pieces.

Alex can’t relocate any of the pieces. Neither he can place any piece on top of other.

### Sample Input:

    4
    5
    6
    7
    8

### Sample Output:

    6
    9
    12
    16

### Explanation:

The explanation below is for the first two test-cases. The rest of them follow a similar logic.

![Diagram](https://hr-challenge-images.s3.amazonaws.com/halloween-party.jpg)

For the first test-case where K = 5,You need 3 Horizontal and 2 vertical cuts. 

halloweenboard For the second test-case where K = 6,You need 3 Horizontal and 3 vertical cuts.
