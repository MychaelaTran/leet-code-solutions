class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None: 
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None: 
        #dont need to check slow bc alr checking fast
            slow = slow.next
            if fast.next.next: 
                fast = fast.next.next
            else: 
                return False
            if slow == fast:
                return True
        return False
