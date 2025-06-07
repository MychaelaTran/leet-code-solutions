# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        node = None
        if head is None: 
            return None
        
        print(head)

        
        while curr: 
            nextt = curr.next
            curr.next = node
            node = curr
            curr = nextt
           
        
        return node


        