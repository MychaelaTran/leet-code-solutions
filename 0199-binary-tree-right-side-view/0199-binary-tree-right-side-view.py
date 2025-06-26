# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return [] 

        q = deque([root])
        ans = []
        
        while q: 
            lvl_length = len(q)

            for i in range(lvl_length): 
                node = q.popleft()
                if i == lvl_length - 1: #very end of lvl 
                    ans.append(node.val)
                
                if node.left: 
                    q.append(node.left)
                
                if node.right: 
                    q.append(node.right)
        return ans 

        
        