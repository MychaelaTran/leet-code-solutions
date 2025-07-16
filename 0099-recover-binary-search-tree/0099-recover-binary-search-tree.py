# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: 
            return root
        
        before = []
        
        def inOrder(node):
            if node is None: 
                return 
            inOrder(node.left)
            before.append(node)
            inOrder(node.right)

        inOrder(root) #inorder traversal
        sorted_arr = sorted(node.val for node in before)

        #swap nodes
        for i in range(len(before)):
            before[i].val = sorted_arr[i]

 
        return  

        

        