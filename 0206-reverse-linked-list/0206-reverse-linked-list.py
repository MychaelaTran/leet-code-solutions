# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: 
            return None
            
        back = None
        curr = head
        new_head = ListNode()
        while curr is not None: 
            node = ListNode()
            node.val = curr.val
            node.next = back
            back = node
            curr = curr.next
        
        
        return back