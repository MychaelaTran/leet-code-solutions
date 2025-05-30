# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: #when go through both if reach end and is None, return None
            return None

        currA = headA
        currB = headB

        while currA != currB:
            if currA is not None:
                currA = currA.next
            else: 
                currA = headB
            
            if currB is not None:
                currB = currB.next
            else: 
                currB = headA
            
        return currA #if no intersection, only time they're equal is when both are None at the end
           