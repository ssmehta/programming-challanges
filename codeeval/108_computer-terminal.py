#!/usr/bin/env python

"""
Computer Terminal

Challenge Description:

In this problem you are writing the software for a small terminal with a 10-row, 10-column display (perhaps for a point-of-sale terminal). Rows and columns are numbered 0 through 9. The character that introduces a control sequence is ^ , the circumflex. The character (or in one case, the two characters) immediately following the control sequence introducer will direct your software in performing its special functions. Here is the complete list of control sequences you will need to interpret: 

^c - clear the entire screen; the cursor row and column do not change 
^h - move the cursor to row 0, column 0; the image on the screen is not changed 
^b - move the cursor to the beginning of the current line; the cursor row does not change 
^d - move the cursor down one row if possible; the cursor column does not change 
^u - move the cursor up one row, if possible; the cursor column does not change 
^l - move the cursor left one column, if possible; the cursor row does not change 
^r - move the cursor right one column, if possible; the cursor row does not change 
^e - erase characters to the right of, and including, the cursor column on the cursor's row; the cursor row and column do not change 
^i - enter insert mode 
^o - enter overwrite mode 
^^ - write a circumflex (^) at the current cursor location, exactly as if it was not a special character; this is subject to the actions of the current mode (insert or overwrite) 
^DD - move the cursor to the row and column specified; each D represents a decimal digit; the first D represents the new row number, and the second D represents the new column number 

No illegal control sequences will ever be sent to the terminal. The cursor cannot move outside the allowed screen locations (that is, between row 0, column 0 and row 9, column 9).

When a normal character (not part of a control sequence) arrives at the terminal, it is displayed on the terminal screen in a manner that depends on the terminal mode. When the terminal is in overwrite mode (as it is when it is first turned on), the received character replaces the character at the cursor's location. But when the terminal is in insert mode, the characters to the right of and including the cursor's location are shifted right one column, and the new character is placed at the cursor's location; the character previously in the rightmost column of the cursor's row is lost. 

Regardless of the mode, the cursor is moved right one column, if possible.

Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

    ^h^c
    ^04^^
    ^13/ \^d^b  /   \\
    ^u^d^d^l^l^l^l^l^l^l^l^l
    ^r^r^l^l^d<CodeEval >^l^l^d/^b \\
    ^d^r^r^66/^b  \\
    ^b^d   \ /
    ^d^l^lv^d^b===========^i^94O123456
    789^94A=======^u^u^u^u^u^u^l^l\\^o^b^r/

Output sample:

Print results in the following way.

        ^
       / \
      /   \
     /     \
    <CodeEval>
     \     /
      \   /
       \ /
        v
    ====A=====
"""

import sys


N = 10


def process_line(s):
    i = 0
    cmds = []
    
    while i < len(s):
        if s[i] == '^':
            if s[i + 1].isdigit():
                cmds.append(s[i : i + 3])
                i += 3
            else:
                cmds.append(s[i : i + 2])
                i += 2
        else:
            j = 1
            
            while i + j < len(s) and s[i + j] != '^':
                j += 1
            
            cmds.append(s[i : i + j])
            i += j
    
    return cmds


def execute_cmds(cmds, display = None, posx = 0, posy = 0, overwrite = True):
    if not display:
        display = [[' ' for _ in range(N)] for _ in range(N)]
    
    for cmd in cmds:
        if cmd[0] == '^':
            if cmd[1] == 'c':
                display = [[' ' for _ in range(N)] for _ in range(N)]
            elif cmd[1] == 'h':
                posx = posy = 0
            elif cmd[1] == 'b':
                posx = 0
            elif cmd[1] == 'd':
                posy = min(posy + 1, N - 1)
            elif cmd[1] == 'u':
                posy = max(posy - 1, 0)
            elif cmd[1] == 'l':
                posx = max(posx - 1, 0)
            elif cmd[1] == 'r':
                posx = min(posx + 1, N - 1)
            elif cmd[1] == 'e':
                display[posy][posx : N] = [' '] * (N - posx)
            elif cmd[1] == 'i':
                overwrite = False
            elif cmd[1] == 'o':
                overwrite = True
            elif cmd[1] == '^':
                display[posy][posx] = '^'
                posx = min(posx + 1, N - 1)
            else:
                posy, posx = int(cmd[1]), int(cmd[2])
        
        else:
            if overwrite:
                display[posy][posx : posx + len(cmd)] = cmd
            else:
                display[posy][posx : posx] = cmd
            
            posx = min(posx + len(cmd), N - 1)
    
    return display, posx, posy, overwrite


if __name__ == '__main__':
    display = [[' ' for _ in range(N)] for _ in range(N)]
    cmds = []
    
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip().replace('\\\\', '\\').replace('CodeEval ', 'CodeEval')
            cmds.extend(process_line(line))
    
    display, _, _, _ = execute_cmds(cmds)
    
    for i in range(N):
        print(''.join(display[i][:N]))
