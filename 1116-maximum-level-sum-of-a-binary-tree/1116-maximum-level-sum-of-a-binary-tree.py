# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right: 
            return 1
        
        q = deque([root])
        maxx = -1000000000000000000
        ans = 1
        lvl = 1
        while q: 
            lvl_length = len(q)
            temp = 0
            

            #traverse level 
            for i in range(lvl_length):
                node = q.popleft()
                temp += node.val

                if node.right: 
                    q.append(node.right)
                
                if node.left:
                    q.append(node.left)
            
            if temp > maxx: 
                maxx = temp
                ans = lvl 
            
            lvl += 1 #add for next level 
            temp = 0 #reset for next level
        
        return ans
            
        