# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node, direction, length):
            if not node:
                return
            #update the gloval max
            self.max_len = max(self.max_len, length)

            if direction == -1:
                dfs(node.left, 1, length + 1)
                dfs(node.right, -1, 1)  #check from right child zigzag
            else:  # direction == 'right'
                dfs(node.right, -1, length + 1)
                dfs(node.left, 1, 1)  #check from ;eft child zigzag

        dfs(root.left, 1, 1)  
        dfs(root.right, -1, 1)  

        return self.max_len