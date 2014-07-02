A Journey to the Moon
=====================

The member states of the UN are planning to send two people to the Moon. But there is a problem. In line with their principles of global unity, they want to pair astronauts in such a way, that both are citizens of different countries.
There are N astronauts numbered with identifiers from 0 to N-1. They are qualified and trained to be sent to the moon. But the trouble is that those in charge of the mission haven’t been directly informed about the citizenship of each astronaut. The only information they have is that some particular pairs of astronauts belong to the same country.

Your task is to compute in how many ways they can pick a pair of astronauts satisfying the above criteria, to be sent to the moon. Assume that you are provided enough pairs to let you identify the groups of astronauts even though you might not know their country directly. For instance, if 1,2,3 are astronauts from the same country; it is sufficient to mention that (1,2) and (2,3) are pairs of astronauts from the same country without providing information about a third pair (1,3). 

### Input:

The first line contains two integers, N and I separated by a single space. I lines follow. each line contains 2 integers separated by a single space A and B such that

    0 <= A, B <= N - 1

and A and B are astronauts from the same country.

### Output:

An integer containing the number of permissible ways in which a pair of astronauts can be sent to the moon.

### Constraints:

* 1 <= N <= 10<sup>5</sup>
* 1 <= I <= 10<sup>6</sup>

### Sample Input:

    4 2
    0 1
    2 3

### Sample Output:

    4

### Explanation:

As persons numbered 0 and 1 belong to same country and 2 and 3 belong to same country. So the UN can choose one person of 0,1 and one out of 2,3. So number of ways of choosing pair is 4.
