# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root is None: 
            return []
        
        return self.helper(root, answer)
        
    
    def helper(self, root, answer):
        if root is None: 
            return []
        
        self.helper(root.left, answer)
        answer.append(root.val)
        self.helper(root.right, answer)

        return answer


    
