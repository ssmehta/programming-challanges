#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        s = sys.stdin.readline().strip()

        if s == s[:: -1]:
            print(-1)
        else:
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]:
                    x = s[: i] + s[i + 1 :]
                    print(i if x == x[:: -1] else (len(s) - i - 1))
                    break
            else:
                print(0)