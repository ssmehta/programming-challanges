#!/usr/bin/env python

import collections, sys


MOD = 1000000007


def connected_components(lists):
    """http://stackoverflow.com/a/14917240/406772"""
    neighbors = collections.defaultdict(set)
    seen = set()
    
    for each in lists:
        for item in each:
            neighbors[item].update(each)
    
    def component(node, neighbors=neighbors, seen=seen, see=seen.add):
        nodes = set([node])
        next_node = nodes.pop
        while nodes:
            node = next_node()
            see(node)
            nodes |= neighbors[node] - seen
            yield node
    
    for node in neighbors:
        if node not in seen:
            yield sorted(component(node))


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    
    if N < 3:
        print(0)
    
    else:
        # Get all of the black edges
        edges = []
    
        for _ in range(N - 1):
            line = sys.stdin.readline().strip()
            
            if line.endswith('b'):
                edges.append(list(map(int, line[:-2].split())))
    
        # Construct subtrees comprised entirely of black edges
        subtrees = connected_components(edges)
    
        # Count number of invalid triplets
        invalid = sum(len(t) * (len(t) - 1) * (3 * N - 2 * len(t) - 2) // 6 for t in subtrees)
        
        # Total number of triplets
        total = N * (N - 1) * (N - 2) // 6
        
        # Print the number of valid triplets
        print((total - invalid) % MOD)