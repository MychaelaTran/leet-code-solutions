# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.helper(root, answer)
        return answer
    
    def helper(self, node, answer):
        if node is None:
            return
        answer.append(node.val)
        self.helper(node.left, answer)
        self.helper(node.right, answer)
