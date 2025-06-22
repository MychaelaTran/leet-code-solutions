from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = [0]
        pathSum = defaultdict(int)
        pathSum[0] = 1 

        def find(node, currSum):
            if not node:
                return

            currSum += node.val
            ans[0] += pathSum[currSum - targetSum]
            pathSum[currSum] += 1

            find(node.left, currSum)
            find(node.right, currSum)

            pathSum[currSum] -= 1  #not use in other side tree calls 

        find(root, 0)
        return ans[0]
