class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        sl = list(s)
        for char in sl:
            if char == "*": 
                stack.pop()
            else: 
                stack.append(char)
        
        s = "".join(stack)
        return s
        