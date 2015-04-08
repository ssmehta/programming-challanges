#!/usr/bin/env python

import collections, sys


MOD = 1000000007 


def dfs_compute(tree, weights, root):
    visited = set()
    stack = [(-1, root)]
    
    product = 1

    while stack:
        parent, node = stack.pop()

        if node not in visited:
            visited.add(node)

            product *= weights[node - 1] - (weights[parent - 1] if parent > -1 else 0)
            product %= MOD

            for child in tree[node] - visited:
                stack.append((node, child))

    return product


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    W = list(map(int, sys.stdin.readline().split()))
    
    tree = collections.defaultdict(set)
    
    for _ in range(N - 1):
        x, y = list(map(int, sys.stdin.readline().split()))
        tree[x].add(y)
        tree[y].add(x)
    
    print(dfs_compute(tree, W, 1))