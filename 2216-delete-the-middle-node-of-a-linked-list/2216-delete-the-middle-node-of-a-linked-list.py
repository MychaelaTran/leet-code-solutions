# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #find mid element
        #one ptr goes 2x speed
        #one goes 1x speed
        #once 2x speed reaches end, 1x speed at middle 
        curr1 = head
        curr2 = head
        if curr2.next is None or head is None:
            return None

        #only look 3 ahead bc of odd length list to round up
        while curr2 and curr2.next and curr2.next.next and curr2.next.next.next: 
            curr1 = curr1.next
            curr2 = curr2.next.next

        
        #curr1 node is node BEFORE we need to delete
        #repoint the curr1 
        curr1.next = curr1.next.next

        return head
        