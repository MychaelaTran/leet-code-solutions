# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: 
            return False

        if root.left is None and root.right is None and root.val != targetSum: 
            return False
        
        if root.left is None and root.right is None and root.val == targetSum: 
            return True
        

        toFind =  targetSum - root.val
        left = self.helper(root.left, toFind)
        right = self.helper(root.right, toFind)

        return left or right

    def helper(self, root, toFind):
        if root is not None: 
            if root.left is None and root.right is None and root.val == toFind: #make sure its leaf node
                return True


            if root.right is not None and root.left is not None:
                return self.helper(root.right, toFind - root.val) or self.helper(root.left, toFind - root.val)

            if root.left is not None:
                print("Entered when root.val is ", root.val)
                print("and to find is: ", toFind)
                return self.helper(root.left, toFind - root.val)
            
            if root.right is not None: 
                return self.helper(root.right, toFind - root.val)
        
        return False

    
        