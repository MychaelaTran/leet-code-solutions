# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head

        odd = head
        even = head.next
        even_later = even #atttach odd to even later 

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
           
        
        #link last odd node to first even node  
        odd.next = even_later
        return head