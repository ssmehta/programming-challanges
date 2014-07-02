Game of Thrones - II
====================

Now that the king knows how to find out whether a given word has an anagram which is a palindrome or not, he is faced with another challenge. He realizes that there can be more than one anagram which are palindromes for a given word. Can you help him find out how many anagrams are possible for a given word which are palindromes?

The king has many words. For each given word, the king needs to find out the number of anagrams of the string which are palindromes. As the number of anagrams can be large, the king needs number of anagrams % (10<sup>9</sup> + 7).

### Input:

A single line which will contain the input string

### Output:

A single line containing the number of anagram strings which are palindrome % (10<sup>9</sup> + 7).

### Constraints:

* 1 <= length of string <= 10<sup>5</sup>
* Each character of the string is a lowercase alphabet.
* Each testcase has atleast 1 anagram which is a palindrome.

### Sample Input 01:

    aaabbbb

### Sample Output 01:

    3

### Explanation:

Three permutation of given string which are palindrome can be given as abbabba, bbaaabb and bababab.

### Sample Input 02:

    cdcdcdcdeeeef

### Sample Output 02:

    90
