from collections import deque 
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([root])
        direction = "left"

        while q: 
            lvl_length = len(q)
            temp = []
            nxt_lvl = deque()

            for _ in range(lvl_length):
                node = q.popleft()  
                if not node:
                    continue
                temp.append(node.val)

                if node.left:
                    nxt_lvl.append(node.left)
                if node.right:
                    nxt_lvl.append(node.right)

            ans.append(temp if direction == "left" else temp[::-1])
            q = nxt_lvl
            direction = "right" if direction == "left" else "left"
        
        return ans

