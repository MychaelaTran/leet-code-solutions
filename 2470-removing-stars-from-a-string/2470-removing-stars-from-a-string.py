class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:  # No need to convert to list
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
