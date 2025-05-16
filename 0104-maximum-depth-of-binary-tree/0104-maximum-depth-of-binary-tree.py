# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        height = 2
        left = 0
        right = 0

        if root.left is not None: 
            left = self.helper(root.left, height)

        if root.right is not None: 
            right = self.helper(root.right, height)
        
        return max(left, right)


    def helper(self, root, height):
        if root is not None:
            if root.left is not None and root.right is not None: 
                height += 1
                return max(self.helper(root.left, height), self.helper(root.right , height))
            
            if root.left is not None:
                height += 1
                return self.helper(root.left, height)
            
            if root.right is not None:
                height += 1
                return self.helper(root.right, height)
            
            return height 
        else: 
            return height 
        