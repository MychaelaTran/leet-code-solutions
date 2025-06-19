# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []
        if root1 is None or root2 is None: 
            return False
        
        if root1.left is None and root1.right is None: 
            if root2.left is None and root2.right is None: 
                return root1.val == root2.val

        def findLeaf(node, arr): 
            if node is None: 
                return
            if node.left is None and node.right is None:
                arr.append(node.val)
            else: 
                findLeaf(node.left, arr)
                findLeaf(node.right, arr)

        findLeaf(root1, ans1)
        findLeaf(root2, ans2)


        return ans1 == ans2
