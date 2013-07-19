#!/usr/bin/python

import sys


languages = [
    'C', 'CPP', 'JAVA', 'PYTHON', 'PERL', 'PHP', 'RUBY', 'CSHARP', 'HASKELL',
    'CLOJURE', 'BASH', 'SCALA', 'ERLANG', 'CLISP', 'LUA', 'BRAINFUCK', 'JAVASCRIPT',
    'GO', 'D', 'OCAML', 'R', 'PASCAL', 'SBCL', 'DART', 'GROOVY', 'OBJECTIVEC'
]

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    for i in range(N):
        language = sys.stdin.readline().strip().split()[1].upper()
        print('VALID' if language in languages else 'INVALID')
