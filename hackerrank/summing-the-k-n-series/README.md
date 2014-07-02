Summing the K-N Series
======================

You are given a series, whose n<sup>th</sup> term is defined as

T<sub>n</sub> = n<sup>K</sup>

You have to find the Sum of the series S<sub>n</sub> = T<sub>1</sub> + T<sub>2</sub> + T<sub>3</sub> + ... + T<sub>n</sub>

Find S<sub>n</sub> % (10<sup>9</sup> + 7)

### Input:

First line contains `T`, denoting the number of testcases.

Each test case contains 1 line:

`n K`

### Output:

Print the required sum % (10<sup>9</sup> + 7).

### Constraints:

* 1 <= T <= 10
* 1 <= K <= 10<sup>3</sup>
* 1 <= n <= 10<sup>16</sup>

### Sample Input:

    3
    5 3
    4 2
    4 1

### Sample Output:

    225
    30
    10

### Explanation:

Case #00: We have 225 = 1<sup>3</sup> + 2<sup>3</sup> + 3<sup>3</sup> + 4<sup>3</sup> + 5<sup>3</sup>

Case #01: We have 30 = 1<sup>2</sup> + 2<sup>2</sup> + 3<sup>2</sup> + 4<sup>2</sup>

Case #02: We have 10 = 1<sup>1</sup> + 2<sup>1</sup> + 3<sup>1</sup> + 4<sup>1</sup>
