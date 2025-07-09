# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #use bfs
        if root is None: 
            return True

        q = deque([(root.left, root.right)])
    
        while q: 
            n1, n2 = q.popleft()
            if not n1 and not n2: continue
            elif not n1 or not n2:
                return False
            else: 
                if n1.val != n2.val: 
                    return False
                q.append((n1.left, n2.right))
                q.append((n1.right, n2.left))
        
        return True
            
        