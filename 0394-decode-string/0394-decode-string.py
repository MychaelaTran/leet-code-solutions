class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        if len(s) <= 0: 
            return s
        
        stack = []
        for char in s: 
            if char != "]":
                stack.append(char)
            else: 
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop() #pop opening
                
                iterator = ""
                while stack and stack[-1].isnumeric():
                    iterator = stack.pop() + iterator
                
                #have whole substring
                stack.append(int(iterator) * temp)

        return "".join(stack)
        