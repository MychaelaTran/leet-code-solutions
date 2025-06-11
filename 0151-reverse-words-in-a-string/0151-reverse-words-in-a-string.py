class Solution:
    def reverseWords(self, s: str) -> str:
        #use a stack 
        split = s.split()
        print(split)
        stack = []
        for word in split: 
            stack = [word] + stack
        
        
        
        return " ".join(stack)