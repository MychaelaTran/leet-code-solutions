# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxx = root.val
        def dfs(node, maxx):
            if node is None:
                return 0
            count = 1 if node.val >= maxx else 0
            new_max = max(maxx, node.val)
            left = dfs(node.left, new_max)
            right = dfs(node.right, new_max)
            return count + left + right
        

        return dfs(root, maxx)
        