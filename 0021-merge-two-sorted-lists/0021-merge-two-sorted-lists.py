# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Both list1 and list2 are sorted in non-decreasing order.
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: 
            return list2
        if list2 is None: 
            return list1

        answer = ListNode()
        if list1.next is None and list2.next is None:
            if list1.val >= list2.val: 
                answer.val = list2.val
                answer.next = ListNode(list1.val)
            else: 
                answer.val = list1.val
                answer.next = ListNode(list2.val)
        elif list1.next is None:
            if list1.val >= list2.val: 
                answer.val = list2.val
                answer.next = self.mergeTwoLists(list1, list2.next)
            else: 
                answer.val = list1.val
                answer.next  = list2
        elif list2.next is None: 
            if list1.val >= list2.val: 
                answer.val = list2.val
                answer.next = list1
            else: 
                answer.val = list1.val
                answer.next  = self.mergeTwoLists(list1.next, list2)
        else: 
            if list1.val >= list2.val:
                answer.val = list2.val
                answer.next = self.mergeTwoLists(list1, list2.next)
            else:
                answer.val = list1.val
                answer.next = self.mergeTwoLists(list1.next, list2)
          

        return answer
        #return answer