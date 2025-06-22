class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        #move n+1 steps to have fast n steps in front of slow 
        for _ in range(n + 1):
            if fast:
                fast = fast.next

        #mpve both until fast reaches teh end
        #slow is n+1 steps behind when fast is none
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next #do this incase head was remoevd
