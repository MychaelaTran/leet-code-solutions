# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        if head is None: 
            return 0 

        if head.next is None: 
            return head.val
        
        if head.next.next is None: 
            return head.val +  head.next.val

        stack =[]
        slow = head
        fast = head

        while fast.next.next is not None: 
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        stack.append(slow.val)
 
        slow = slow.next
        while slow: 
            temp = stack.pop() + slow.val
            if temp > ans: 
                ans = temp
            slow = slow.next


        return ans
        