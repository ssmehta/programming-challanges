Angry Children
==============

Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has *N* packets of candies and would like to distribute one packet to each of the *K* children in the village (each packet may contain different number of candies). To avoid a fight between the children, he would like to pick *K* out of *N* packets such that the unfairness is minimized.

Suppose the K packets have (X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>, ..., X<sub>k</sub>) candies in them, where x<sub>i</sub> denotes the number of candies in the i<sup>th</sup> packet, then we define *unfairness* as

**max(X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>k</sub>) - min(X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>k</sub>)**

where *max* denotes the highest value amongst the elements and *min* denotes the least value amongst the elements. Can you figure out the minimum *unfairness* and print it?

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

    20

### Explanation #00:

Here K = 3.  We can choose packets that contain 10, 20, 30 candies. The unfairness is

    max(10, 20, 30) - min(10, 20, 30) = 30 - 10 = 20

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

    3

#### Explanation #01:

Here K = 4.  We can choose the packets that contain 1, 2, 3, 4 candies. The unfairness is

    max(1, 2, 3, 4) - min(1, 2, 3, 4) = 4 - 1 = 3
