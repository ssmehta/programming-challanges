A Chocolate Fiesta
==================

Welcome to the exciting class of Professor Manasa. In each lecture she used to play some game while teaching a new concept. Today’s topic is Set Theory. For today’s game, she had given a set *A = {a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>N</sub>}* of *N* integers to her students and asked them to play the game as follows.

At each step of the game she calls a random student and asks him/her to select a non-empty subset from set *A* such that this subset had not been selected earlier and the sum of subset should be even. This game ends when all possible subsets had been selected. Manasa needs your help in counting the total number of times students can be called assuming each student gives the right answer. **While it is given that if two numbers are same in the given set, they have different colors. It means that if a<sub>1</sub> = a<sub>2</sub>, then choosing a<sub>1</sub> and choosing a<sub>2</sub> will be considered as different sets.**

**Note:**

1. Two subsets are different if there exists an element *(a<sub>k</sub>)* that is present in one subset but not in other. Let’s say set *A = {a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>} = {2, 2, 3}*, then all possible subsets are *{}, {a<sub>1</sub>}, {a<sub>2</sub>}, {a<sub>3</sub>}, {a<sub>1</sub>, a<sub>2</sub>}, {a<sub>1</sub>, a<sub>3</sub>}, {a<sub>2</sub>, a<sub>3</sub>}, {a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>}* which is equivalent to *{}, {2}, {2}, {3}, {2, 2}, {2, 3}, {2, 3}, {2, 2, 3}*.

2. Students can be called multiple times.

### Input:

The first line contains an integer *N* i.e. size of set *A*.

Next line will contain *N* integers, each representing an element of *A*.

### Output:

Print number of time students are called. As this number can be very large you have to print the answer modulo (10<sup>9</sup> + 7).

### Constraints:

* 1 <= *N* <= 10<sup>5</sup>
* 0 <= *a<sub>i</sub>* <= 10<sup>4</sup>, where *i ∈ [1..N]*

### Sample Input #00:

    4
    2 4 6 1

### Sample Output #00:

    7

### Sample Input #01:

    3
    1 2 2

### Sample Output #01:

    3

### Explanation:

There are 7 different ways in which a non-empty subset, with even sum, can be selected, i.e., *{2}, {4}, {6}, {2, 4}, {2, 6}, {4, 6}, {2, 4, 6}*.

For second sample test case, there are 3 different ways in which a non-empty subset, with even sum, can be selected, i.e., *{a<sub>2</sub>}, {a<sub>3</sub>}, {a<sub>2</sub>, a<sub>3</sub>}* which is equivalent to *{2}, {2}, {2,2}*.
