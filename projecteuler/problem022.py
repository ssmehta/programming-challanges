#!/usr/bin/env python

"""
Problem 022:

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multipl this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""


letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

with open('problem022-names.txt') as f:
    names = f.read().replace('"', '').split(',')
    names.sort()
    
    score = lambda s: sum(letters.index(c) + 1 for c in s)
    print(sum((i + 1) * score(name) for i, name in enumerate(names)))
