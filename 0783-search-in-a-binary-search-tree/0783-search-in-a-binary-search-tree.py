# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: 
            return None
        
        if root.val == val: 
            return root 
        else: 
            if root.left and root.right: 
                return self.searchBST(root.left, val) or self.searchBST(root.right, val)
            elif root.right: 
                return self.searchBST(root.right, val)
            else: 
                return self.searchBST(root.left, val)
        