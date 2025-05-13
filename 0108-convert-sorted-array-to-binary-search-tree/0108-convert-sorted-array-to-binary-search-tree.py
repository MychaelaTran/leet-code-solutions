# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        length = len(nums)
        return self.helper(0, length-1, nums)

    def helper(self, start, end, nums):
        if start > end:
            return None

        rootIndex = (start + end)//2
        root = TreeNode()
        root.val = nums[rootIndex]

        root.left = self.helper(start, rootIndex-1, nums)
        root.right = self.helper(rootIndex  + 1, end, nums)

        return root