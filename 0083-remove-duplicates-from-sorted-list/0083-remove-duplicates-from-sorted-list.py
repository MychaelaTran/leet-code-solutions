# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        current = head
        while current is not None and current.next != None: 
            if current.val not in seen:
                seen.add(current.val)
                current = current.next
            else: 
                current.val = current.next.val
                current.next = current.next.next

        #if the last node is a duplicate
        if not current: 
            return None 
            
        if current.val in seen: 
            #remove this node
            prevNode = head
            if prevNode == current:
                return None
            while prevNode.next!= current:
                prevNode = prevNode.next
            prevNode.next = None

        return head
   