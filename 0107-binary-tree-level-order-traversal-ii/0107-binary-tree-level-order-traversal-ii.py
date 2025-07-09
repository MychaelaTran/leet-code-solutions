# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None: 
            return ans 
        
        q = deque([root])
        while q: 
            lvl_length = len(q)
            temp = []
            for _ in range(lvl_length): 
                node = q.popleft()
                temp.append(node.val)

                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            
            if len(temp) > 0: 
                ans.append(temp)
        
        return ans[::-1]

        