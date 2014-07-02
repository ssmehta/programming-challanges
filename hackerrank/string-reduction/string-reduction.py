#!/usr/bin/env python

import collections, sys


char_set = 'abc'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        chars = sys.stdin.readline().lower().strip()
        count = collections.Counter(chars)
        
        # Set up list of count parities
        parities = [v % 2 for v in count.values()]
        while len(parities) < len(char_set):
            parities.append(0)
        
        
        # Check if the string is irreducible
        if len(count.values()) == 1:
            print(len(chars))
        
        # If the instances of each character have the same parity, then since
        # the reduction steps flip each count's parity each will share the same
        # parity throughout the reduction.  
        #
        # Clearly, any reducible string much have a solution with len(solution)
        # < len(chars). We will show further that the answer must be less than 3.
        # 
        # Suppose, by contradiction, that we have a non-reducible answer with
        # length 3 <= len(solution) < len(chars).  For simplicity, take 'aaa' as
        # our solution. This must have been reduced from a string containing an
        # adjacent 'BC' term.  However, any case we find that the string is 
        # further reducible:
        #     bcaaa -> bbaa -> bca -> aa
        #     abcaa -> ccaa -> cba -> aa
        #     aaabc -> aacc -> abc -> aa
        # This contradicts out initial assertion of the string's irreducibility,
        # and therefore we must have that len(solution) < 3.
        # 
        # Back to this case, where the parity of all counts matches, our fully
        # reduced solution must then correspond to [0, 0, 2].
        elif len(set(parities)) == 1:
            print(2)
        
        # Otherwise, pigeonhole says that two will have the same parity, and
        # the other will have the opposite.  This will continue throughout
        # reduction, resulting in two even and one odd which corresponds to
        # [0, 0, 1].
        else:
            print(1)
