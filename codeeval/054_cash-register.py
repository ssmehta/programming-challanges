#!/usr/bin/env python

"""
Cash Register

Challenge Description:

The goal of this challenge is to design a cash register program. You will be given two float numbers. The first is the purchase price (PP) of the item. The second is the cash (CH) given by the customer. Your register currently has the following bills/coins within it:

    'PENNY': .01,
    'NICKEL': .05,
    'DIME': .10,
    'QUARTER': .25,
    'HALF DOLLAR': .50,
    'ONE': 1.00,
    'TWO': 2.00,
    'FIVE': 5.00,
    'TEN': 10.00,
    'TWENTY': 20.00,
    'FIFTY': 50.00,
    'ONE HUNDRED': 100.00

The aim of the program is to calculate the change that has to be returned to the customer.

Input sample:

Your program should accept as its first argument a path to a filename. The input file contains several lines. Each line is one test case. Each line contains two numbers which are separated by a semicolon. The first is the Purchase price (PP) and the second is the cash (CH) given by the customer. eg.

    15.94;16.00
    17;16
    35;35
    45;50

Output sample:

For each set of input produce a single line of output which is the change to be returned to the customer. In case the CH < PP, print out ERROR. If CH == PP, print out ZERO. For all other cases print the amount that needs to be returned, in terms of the currency values provided. The output should be sorted in highest-to-lowest order (DIME,NICKEL,PENNY). eg.

    NICKEL,PENNY
    ERROR
    ZERO
    FIVE
"""

import sys


currency = {
    1: 'PENNY', 5: 'NICKEL', 10: 'DIME', 25: 'QUARTER', 50: 'HALF DOLLAR',
    100: 'ONE', 200: 'TWO', 500: 'FIVE', 1000: 'TEN', 2000: 'TWENTY',
    5000: 'FIFTY', 10000: 'ONE HUNDRED'
}


if __name__ == '__main__':
    parse_currency = lambda s: int(s.replace('.', '')) if '.' in s else 100 * int(s)
    
    with open(sys.argv[1]) as f:
        for line in f:
            if line.strip():
                PP, CH = [parse_currency(s) for s in line.split(';')]
                change = []
                
                if PP == CH:
                    print('ZERO')
                elif CH < PP:
                    print('ERROR')
                else:
                    diff = CH - PP
                    
                    for x in sorted(currency, reverse = True):
                        while diff // x > 0:
                            diff -= x
                            change.append(currency[x])
                    
                    print(','.join(change))
