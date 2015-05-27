UK and US
=========

US english and UK english differ in many aspects. One such aspect is the aversion towards use of **ze** instead of **se** as used in the UK. Given the US format of a word that ends with **ze** your task is to findout the count of all its UK and US variant in all the given sequence.

### Input:

First line contains N, N lines follow each line contains a sequence of words (W) separated by a single space. Next line contains T. T testcases follow in a new line. Each line contains the **US** spelling of a word (W’)

### Constraints:

* 1 <= N <= 5
* Each line doesn’t contain more than 10 words (W)
* Each character of W and W’ is a lowercase alphabet.
* If C is the count of the number of characters of W or W’, then
* 1 <= C <= 20
* 1 <= T <= 5
* W’ ends with ze ( US version of the word)

### Output:

Output T lines and in each line output the number of UK and US version of (W’) in all of N lines that contains a sequence of words.

### Sample Input:

    2
    hackerrank has such a good ui that it takes no time to familiarise its environment
    to familiarize oneself with ui of hackerrank is easy
    1
    familiarize

### Sample Output:

    2

### Explanation:

In the given 2 lines, we find familiarize and familiarise once each. So, the total count is 2.
