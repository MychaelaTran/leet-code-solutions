# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: 
            return None
        
        if head.next is None: 
            return head
        
        dummy = ListNode(0,head)
        prev, curr = dummy, head

        while curr and curr.next: #make sure we have 2 more nodes to swap  
            next_start = curr.next.next
            snd = curr.next
            
            #the reversing 
            snd.next = curr
            curr.next = next_start
            prev.next = snd

            #update the ptrs
            prev = curr
            curr = next_start        
        
        return dummy.next

'''
1234

prev = 0
curr = 1
snd = 2
next_start = 3

snd.next = curr : 2 -> 1
curr.next = next_start : 1 -> 3
prev.next = snd : 0 -> 2 ... means getting 
'''


        