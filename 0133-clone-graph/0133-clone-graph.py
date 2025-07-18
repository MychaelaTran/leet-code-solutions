"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: 
            return node 
        
        q = deque([node])
        clone = {}
        clone[node] = Node(node.val) #acts as a "visited"
                                     #that maps node to node val 

        while q: 
            curr = q.popleft()
            for n in curr.neighbors: 
                if n not in clone:
                    clone[n] = Node(n.val) 
                    q.append(n)
                clone[curr].neighbors.append(clone[n])

        return clone[node]
        

        