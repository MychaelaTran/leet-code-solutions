"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: 
            return root
        
        q = deque([root])
        while q:
            lvl_len = len(q)
            for i in range(lvl_len): 
                node = q.popleft()
                if i < lvl_len -1: 
                    node.next = q[0]
                else: 
                    node.next = None

                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)  

        return root                   
        