# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        #make fast n steps in front of slow
        #so when fast reaches end, we are at node before remove slow
        for _ in range(n):
            fast = fast.next  

        # move both until fast is at the last node
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next #in case head deleted



        