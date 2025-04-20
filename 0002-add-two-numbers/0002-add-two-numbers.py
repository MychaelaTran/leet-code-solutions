# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        curr1 = l1
        curr2 = l2
        print("this is l1", l1)
        #while loops to make the LL into list 
        while curr1 is not None:
            num1.append(curr1.val)
            curr1 = curr1.next

        while curr2 is not None:
            num2.append(curr2.val)
            curr2 = curr2.next

        #reverse them 
        num1.reverse()
        num2.reverse()

        num1r = int("".join((map(str, num1))))  #use map to make into string then join them together using join, sperating thjem withj nothing ""
        num2r = int("".join((map(str, num2))))
        result = num1r + num2r
    
        #make result back inti list
        list_str = list(str(result))
        list_str.reverse() #reverse
        answer = list(map(int, list_str)) #maps all to int and then need to wrap in list bc map returns an obj so make returnm lsit
        print(answer)
        #make back into type ListNode
        list_node = ListNode()
        curr = list_node
        for i in range(len(answer)): 
            if i == len(answer) -1:
                curr.val = answer[i]
            else: 
                curr.val = answer[i]
                curr.next = ListNode()
                curr = curr.next
        print("this is answer", list_node)
        return list_node


