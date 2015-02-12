#!/usr/bin/env python

"""
Telephone Words

Challenge Description:

Given a 7 digit telephone number, print out all the possible sequences of letters that can represent the given telephone number. Note that in a standard 12 key pad, 0 and 1 do not have any letters associated with them. They are to be treated as such, i.e. a 0/1 in the telephone number will be retained in the final word as well. You may use the following mapping between numbers and characters:

    0 => 0
    1 => 1
    2 => abc
    3 => def
    4 => ghi
    5 => jkl
    6 => mno
    7 => pqrs
    8 => tuv
    9 => wxyz

Input sample:

Your program should accept as its first argument a path to a filename.The input file contains 7 digit telephone numbers, one per line.

    4155230

Output sample:

Print out the words that can produce the telephone number, alphabetically sorted and comma delimited. eg.

    g1jjad0,g1jjae0,g1jjaf0,g1jjbd0,g1jjbe0,g1jjbf0,g1jjcd0,g1jjce0,g1jjcf0,g1jkad0,g1jkae0,g1jkaf0,g1jkbd0,g1jkbe0,g1jkbf0,g1jkcd0,g1jkce0,g1jkcf0,g1jlad0,g1jlae0,g1jlaf0,g1jlbd0,g1jlbe0,g1jlbf0,g1jlcd0,g1jlce0,g1jlcf0,g1kjad0,g1kjae0,g1kjaf0,g1kjbd0,g1kjbe0,g1kjbf0,g1kjcd0,g1kjce0,g1kjcf0,g1kkad0,g1kkae0,g1kkaf0,g1kkbd0,g1kkbe0,g1kkbf0,g1kkcd0,g1kkce0,g1kkcf0,g1klad0,g1klae0,g1klaf0,g1klbd0,g1klbe0,g1klbf0,g1klcd0,g1klce0,g1klcf0,g1ljad0,g1ljae0,g1ljaf0,g1ljbd0,g1ljbe0,g1ljbf0,g1ljcd0,g1ljce0,g1ljcf0,g1lkad0,g1lkae0,g1lkaf0,g1lkbd0,g1lkbe0,g1lkbf0,g1lkcd0,g1lkce0,g1lkcf0,g1llad0,g1llae0,g1llaf0,g1llbd0,g1llbe0,g1llbf0,g1llcd0,g1llce0,g1llcf0,h1jjad0,h1jjae0,h1jjaf0,h1jjbd0,h1jjbe0,h1jjbf0,h1jjcd0,h1jjce0,h1jjcf0,h1jkad0,h1jkae0,h1jkaf0,h1jkbd0,h1jkbe0,h1jkbf0,h1jkcd0,h1jkce0,h1jkcf0,h1jlad0,h1jlae0,h1jlaf0,h1jlbd0,h1jlbe0,h1jlbf0,h1jlcd0,h1jlce0,h1jlcf0,h1kjad0,h1kjae0,h1kjaf0,h1kjbd0,h1kjbe0,h1kjbf0,h1kjcd0,h1kjce0,h1kjcf0,h1kkad0,h1kkae0,h1kkaf0,h1kkbd0,h1kkbe0,h1kkbf0,h1kkcd0,h1kkce0,h1kkcf0,h1klad0,h1klae0,h1klaf0,h1klbd0,h1klbe0,h1klbf0,h1klcd0,h1klce0,h1klcf0,h1ljad0,h1ljae0,h1ljaf0,h1ljbd0,h1ljbe0,h1ljbf0,h1ljcd0,h1ljce0,h1ljcf0,h1lkad0,h1lkae0,h1lkaf0,h1lkbd0,h1lkbe0,h1lkbf0,h1lkcd0,h1lkce0,h1lkcf0,h1llad0,h1llae0,h1llaf0,h1llbd0,h1llbe0,h1llbf0,h1llcd0,h1llce0,h1llcf0,i1jjad0,i1jjae0,i1jjaf0,i1jjbd0,i1jjbe0,i1jjbf0,i1jjcd0,i1jjce0,i1jjcf0,i1jkad0,i1jkae0,i1jkaf0,i1jkbd0,i1jkbe0,i1jkbf0,i1jkcd0,i1jkce0,i1jkcf0,i1jlad0,i1jlae0,i1jlaf0,i1jlbd0,i1jlbe0,i1jlbf0,i1jlcd0,i1jlce0,i1jlcf0,i1kjad0,i1kjae0,i1kjaf0,i1kjbd0,i1kjbe0,i1kjbf0,i1kjcd0,i1kjce0,i1kjcf0,i1kkad0,i1kkae0,i1kkaf0,i1kkbd0,i1kkbe0,i1kkbf0,i1kkcd0,i1kkce0,i1kkcf0,i1klad0,i1klae0,i1klaf0,i1klbd0,i1klbe0,i1klbf0,i1klcd0,i1klce0,i1klcf0,i1ljad0,i1ljae0,i1ljaf0,i1ljbd0,i1ljbe0,i1ljbf0,i1ljcd0,i1ljce0,i1ljcf0,i1lkad0,i1lkae0,i1lkaf0,i1lkbd0,i1lkbe0,i1lkbf0,i1lkcd0,i1lkce0,i1lkcf0,i1llad0,i1llae0,i1llaf0,i1llbd0,i1llbe0,i1llbf0,i1llcd0,i1llce0,i1llcf0
"""

from __future__ import print_function
import sys


chars = {
    '0': '0', '1': '1', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

def find_words(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return list(chars[s])
    else:
        words = find_words(s[1:])
        return [c + s for c in chars[s[0]] for s in words]
            

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            print(*find_words(line.strip()), sep = ',')
