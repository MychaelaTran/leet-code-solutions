# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        big_head = ListNode()
        big_start = big_head
        dummy = ListNode(0, head) #link 
        prev = dummy
        curr = head

        while curr: 
            nxt = curr.next
            if curr.val >= x: 
                curr.next = None
                prev.next = nxt
                big_start.next = curr
                big_start = curr
            
            else: 
                prev = curr
            curr = nxt
     
        
        prev.next = big_head.next




        return dummy.next

        