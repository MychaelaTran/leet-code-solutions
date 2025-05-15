# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        if root.left is None and root.right is None: 
            return 1

        right = 0 
        left = 0

        height = 1
        if root.left is not None: 
            left = self.helper(root.left, height)
        if root.right is not None: 
            right = self.helper(root.right, height)
        
        if right == 0: 
            right = left
        
        if left == 0: 
            left = right

        return min(left, right) 
    
    def helper(self, root, height):
        if root: 
            if root.left is not None and root.right is not None: 
                height += 1
                return min(self.helper(root.left, height),self.helper(root.right, height))
            elif root.left is None: 
                height += 1
                return self.helper(root.right, height)
            elif root.right is None: 
                height += 1
                return self.helper(root.left, height)
            else:
                return height #leaf node
        else: 
            return height #root is empty 
            
    


        