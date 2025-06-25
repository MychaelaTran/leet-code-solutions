# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #LCA is p or q on same branch side , diff levels
        #LCA is joint node when o n fidfferent sides
        if not root: 
            return None

        if root == p or root == q: 
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r: 
            return root #if both non null
        else: 
            return l or r
        


        