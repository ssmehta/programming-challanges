#!/usr/bin/env python

import sys


NUMBERS = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
    23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty seven',
    28: 'twenty eight', 29: 'twenty nine'
}


if __name__ == '__main__':
    H = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    
    if M == 0:
        print(NUMBERS[H] +' o\' clock')
    elif M == 15:
        print('quarter past '+ NUMBERS[H])
    elif M < 30:
        print(NUMBERS[M] +' minutes past '+ NUMBERS[H])
    elif M == 30:
        print('half past '+ NUMBERS[H])
    elif M == 45:
        print('quarter to '+ NUMBERS[(H + 1) % 12])
    else:
        print(NUMBERS[60 - M] +' minutes to '+ NUMBERS[(H + 1) % 12])