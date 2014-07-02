Building a List
===============

Chan has decided to make a list of all possible combinations of letters of a given string S. If there are two sub-strings with the same set of characters, print the lexicographically smallest arrangement of the sub-string.

    abc acb cab bac bca

all the above sub-strings’ lexicographically smallest string is abc.

Each character in the string S is unique. Your task is to print the entire list of Chan’s in lexicographic order.

for string abc, the list in lexicographic order is given below

    a ab abc ac b bc c

### Input:

The first line contains the number of test cases T. T testcases follow.

Each testcase has 2 lines. The first line is an integer N ( the length of the string).

The second line contains the string S.

### Output:

For each testcase, print the entire list of combinations of string S, with each combination of letters in a newline.

### Constraints:

* 0 < T < 50
* 0 < N < 16
* string S contains only small alphabets (a - z)

### Sample Input:

    2
    2
    ab
    3
    xyz

### Sample Output:

    a
    ab
    b
    x
    xy
    xyz
    xz
    y
    yz
    z

### Explanation:

In the first case we have ab, the possibilities are a, ab and b. Similarly, all combination of characters of xyz.
