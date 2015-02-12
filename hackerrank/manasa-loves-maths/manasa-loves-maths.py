#!/usr/bin/env python

import itertools, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N = sys.stdin.readline().strip()
        
        if len(N) == 1:
            print('YES' if N == '8' or N == '0' else 'NO')
        elif len(N) == 2 :
            print('YES' if (int(N) % 8 == 0 or int(N[::-1]) % 8 == 0) else 'NO')
        else:
            for s in itertools.permutations(N, 3):
                if int(''.join(s)) % 8 == 0:
                    print('YES')
                    break
            else:
                print('NO')