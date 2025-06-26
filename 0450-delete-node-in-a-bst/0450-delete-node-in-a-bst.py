# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #3 cases hibbard deletion 
        #1. delete node by setting parent link to null when its a leaf node
        #2. one child delete node by replacing parent link with deleted node's child lin k
        #3. find successor x of node bby going right then left until null left link 
        #update links and node counts after recurssive calls 

        if not root: 
            return None #key not in tree or tree empty 
        
        if key < root.val: 
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: 
            root.right = self.deleteNode(root.right, key)
        else: #found node to delete  
            #case 1: no childsren 
            if not root.left and not root.right: 
                return None #setting root.l/r = None
            
            #case 2: one child
            if not root.left: 
                return root.right        #    10            Delete 16, make 15 child of 10
            if not root.right:           #  4    16 
                return root.left         #      15  
                                         #     14 
            
            #case 3 two children 
            #find smallest node in rigt subtree and make link 
            new_child = self.findMin(root.right) #find right subtree smallest
            
            root.val = new_child.val #make deleted node's value the new one
            
            #delete new_child node from right subtree bc we moved it up
            root.right = self.deleteNode(root.right, new_child.val)
        
        return root
    
    def findMin(self, node): 
        while node.left: 
            node = node.left
        return node
