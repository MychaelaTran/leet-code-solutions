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
        
        depth = 0
        return self.helper(root)

    

    def helper(self, node):
        if node is None:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        return 1 + max(left, right)


