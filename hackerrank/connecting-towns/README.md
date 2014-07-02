Connecting Towns
================

Gandalf is travelling from **Rohan** to **Rivendell** to meet Frodo but there is no direct route from **Rohan** (T<sub>1</sub>) to **Rivendell** (T<sub>n</sub>).

But there are towns T<sub>2</sub>, T<sub>3</sub>, T<sub>4</sub>, ..., T<sub>n - 1</sub> such that there are N<sub>1</sub> routes from Town T<sub>1</sub> to T<sub>2</sub>, and in general, N<sub>i</sub> routes from T<sub>i</sub> to T<sub>i + 1</sub> for i = 1 to n - 1 and 0 routes for any other T<sub>i</sub> to T<sub>j</sub> for j ≠ i + 1.

Find the total number of routes Gandalf can take to reach Rivendell from Rohan.

### Note:

Gandalf has to pass all the towns T<sub>i</sub> for i = 1 to n - 1 in numerical order to reach Tn.
For each T<sub>i</sub>, T<sub>i + 1</sub> there are only N<sub>i</sub> distinct routes Gandalf can take.

### Input:

The first line contains an integer T, T test-cases follow. 

Each test-case has 2 lines. The first line contains an integer N (the number of towns).
 
The second line contains N - 1 space separated integers where the ith integer denotes the number of routes, N<sub>i</sub>, from the town T<sub>i</sub> to T<sub>i + 1</sub>.

### Output:

Total number of routes from T<sub>1</sub> to T<sub>n</sub> modulo 1234567.

### Constraints:

* 1 <= T <= 1000
* 2 < N <= 100
* 1 <= N<sub>i</sub> <= 1000

### Sample Input:

    2
    3
    1 3
    4
    2 2 2

### Sample Output:

    3
    8

### Explanation:

Case 1: 1 route from T<sub>1</sub> to T<sub>2</sub>, 3 routes from T<sub>2</sub> to T<sub>3</sub>, hence only 3 routes.

Case 2: There are 2 routes from each city to the next, at each city, Gandalf has 2 choices to make, hence 2 * 2 * 2 = 8.
