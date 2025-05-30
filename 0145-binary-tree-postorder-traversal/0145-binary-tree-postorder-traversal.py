# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root is None: 
            return answer
        
        self.helper(root.left, answer)
        self.helper(root.right, answer)
        answer.append(root.val)

        return answer
    
    def helper(self, node, answer):
        if node is None: 
            return 
        
            
        
        self.helper(node.left, answer)
        self.helper(node.right, answer)
        answer.append(node.val)
        
         
        
        
        
