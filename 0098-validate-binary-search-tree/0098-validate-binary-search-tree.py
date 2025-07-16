# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return True

        #inorder traversaL
        traversal = []
        def dfs(node): 
            if not node: 
                return 
            
            dfs(node.left)
            traversal.append(node.val)
            dfs(node.right)
        dfs(root)
        print(traversal)
        sorted_arr = sorted(traversal)
        print(sorted_arr)

        seen = set()
        for i in range(len(traversal)):
            if traversal[i] != sorted_arr[i] or traversal[i] in seen:
                return False
            seen.add(traversal[i])
        
        return True 
        