# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr and curr.next: 
            if curr.val == curr.next.val: 
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else: 
                prev = prev.next
            
            curr = curr.next


        


        return dummy.next
                
        

prev = 2
curr = 4 
after = 4



'''
This is for removing duplicates but keeping one copy
prev = head
        curr = head.next

        while curr.next: 
            if prev.val == curr.val: 
                prev.next = curr.next
            
            prev = curr
            curr = curr.next
            print(head)
        
        return head
'''
            
            