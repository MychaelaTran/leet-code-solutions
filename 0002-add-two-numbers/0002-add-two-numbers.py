# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        ans = ListNode()
        head = ans
        carry = 0

        while p1 is not None or p2 is not None: 
            if p1 is None: 
                p1_val = 0
            else: 
                p1_val = p1.val
            
            if p2 is None: 
                p2_val = 0
            else: 
                p2_val = p2.val

            digit = p1_val + p2_val
            print("this is difit: ", digit)
            ans.val = (digit + carry) % 10
            carry = (digit + carry) // 10

            if p1: 
                p1 = p1.next
            if p2: 
                p2 = p2.next

            if not p1 and not p2: 
                if carry == 0:
                    break
                else: 
                    ans.next = ListNode()
                    ans.next.val = carry
                    break



            ans.next = ListNode()
            ans = ans.next
            
        
        
        print(p1)
        print(p2)
                
        
        print(head)

        return head

        