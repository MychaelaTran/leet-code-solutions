# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        #root to leaf 
        to_find = targetSum 
        curr = root

        def find(node, to_find, arr): 
            if node is None: 
                return ans
            
            if not node.left and not node.right and to_find == node.val: 
                ans.append(arr + [node.val]) # add arr plus node at 
            
            if node.left: 
                find(node.left, to_find - node.val , arr + [node.val])
                #make new arrya for each branch arr + [node.val]
                #modugy to_find only for this recurssive call not node.right too 
            
            if node.right:
                find(node.right, to_find - node.val, arr + [node.val])

        print(find(root, to_find, []))

        return ans 
        