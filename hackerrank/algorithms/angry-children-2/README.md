Angry Children
==============

Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has *N* packets of candies and would like to distribute one packet to each of the *K* children in the village (each packet may contain different number of candies). To avoid a fight between the children, he would like to pick *K* out of *N* packets such that the unfairness is minimized.

Suppose the K packets have (X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>, ..., X<sub>k</sub>) candies in them, where x<sub>i</sub> denotes the number of candies in the i<sup>th</sup> packet, then we define *unfairness* as

    Sum[|X<sub>i</sub> - X<sub>j</sub>|, 1 <= i < j <= k]

where |a| denotes the absolute value of a.

### Input:

The first line contains an integer N.

The second line contains an integer K.  N lines follow each integer containing the candy in the i<sup>th</sup> packet.

### Output:

A single integer which will be the minimum *unfairness*.

### Constraints:

* 1 <= N <= 10<sup>5</sup>
* 1 <= K <= N
* 0 <= number of candies in any packet <= 10<sup>9</sup>

### Sample Input #00:

    7
    3
    10
    100
    300
    200
    1000
    20
    30

### Sample Output #00:

    40

### Explanation #00:

Bill Gates will choose packets having 10, 20 and 30 candies.  So unfairness will be |10 - 20| + |20 - 30| + |10 - 30| = 40.  It will be minimum as compared to any other distribution which can be verified.

### Sample Input #01:

    10
    4
    1
    2
    3
    4
    10
    20
    30
    40
    100
    200

### Sample Output #01:

    10

#### Explanation #01:

Bill Gates will choose 4 packets having 1, 2, 3 and 4 candies.  So, unfairness will be |1 - 2| + |1 - 3| + |1 - 4| + |2 - 3| + |2 - 4| + |3 - 4| = 10.
