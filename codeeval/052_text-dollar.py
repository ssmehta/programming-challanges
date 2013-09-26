#!/usr/bin/env python

"""
Text Dollar

Challenge Description:

Credits: This challenge has been authored by Terence Rudkin

You are given a positive integer number. This represents the sales made that day in your department store. The payables department however, needs this printed out in english. NOTE: The correct spelling of 40 is Forty. (NOT Fourty)

Input sample:

Your program should accept as its first argument a path to a filename.The input file contains several lines. Each line is one test case. Each line contains a positive integer. eg.

    3
    10
    21
    466
    1234

Output sample:

For each set of input produce a single line of output which is the english textual representation of that integer. The output should be unspaced and in Camelcase. Always assume plural quantities. You can also assume that the numbers are < 1000000000 (1 billion). In case of ambiguities eg. 2200 could be TwoThousandTwoHundredDollars or TwentyTwoHundredDollars, always choose the representation with the larger base i.e. TwoThousandTwoHundredDollars. For the examples shown above, the answer would be:

    ThreeDollars
    TenDollars
    TwentyOneDollars
    FourHundredSixtySixDollars
    OneThousandTwoHundredThirtyFourDollars
"""

import sys


base = {
    0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
    7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve',
    13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
    17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
}

tens = {
    2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy',
    8: 'Eighty', 9: 'Ninety'
}

suffix = {0: '', 1: 'Thousand', 2: 'Million', 3: 'Billion', 4: 'Trillion'}

def int_to_text(n):
    def block_to_text(n):
        text = '' if n < 100 else base[n // 100] +'Hundred'
        
        if n % 100 < 10:
            text += base[n % 10]
        elif 10 <= n % 100 <= 19:
            text += base[n % 100]
        else:
            text += tens[(n % 100) // 10] + base[n % 10]
        
        return text
    
    
    text = 'Dollars'
    depth = 0
    
    while n > 0:
        block = block_to_text(n % 1000)
        if block:
            text = block + suffix[depth] + text
        
        n //= 1000
        depth += 1
    
    return text
        


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                print(int_to_text(int(line)))
