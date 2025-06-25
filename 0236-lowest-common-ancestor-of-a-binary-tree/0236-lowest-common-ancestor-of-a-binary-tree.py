class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #base case
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        #serach L an d R
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            #found LCA when p and q diff branches
            return root
        
        #if one side returned nill, return pther side bc same branch
        return left or right


'''
        3
       / \
      5   1
     / \
    6   2


p = 6 and q = 1
start at root. doesnt = 6 or 1
1. Recurse left lowestCommonAncestor(5, 6, 1)
2. Recurse right lowestCommonAncestor(1, 6, 1)

looking at 1. 
5 != 6 and 5 != 1
3.Recurse left: lowestCommonAncestor(6, 6, 1)
4.Recurse right: lowestCommonAncestor(2, 6, 1)

at 3. node 6 == 6
so return node 6

at 4. node 2 doesnt equal 6 or 1 so we return None


now we go back up to root 5
left = 6
right = None
so we return 6 

right subtree 2. 
root == 1 so return 1

Back to node 3
left = 6
right = 3
return root = 3

'''
