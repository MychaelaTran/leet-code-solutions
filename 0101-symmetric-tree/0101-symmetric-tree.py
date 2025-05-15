# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return True

        left = root.left
        right = root.right

        return self.isIdentical(left,right)
    
    def isIdentical(self, p, q) -> bool:
        if p is None and q is None: 
            return True

        if p is None and q is not None: 
            return False

        if q is None and p is not None: 
            return False
        
        #v smillar to #100 but since its mirrored we match them with their mirror ie left to right and right to left 
        if p.val == q.val:
            if self.isIdentical(p.right, q.left) and self.isIdentical(p.left, q.right):
                return True
            else: 
                return False
        return False
        