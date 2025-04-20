class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in "([{":
                stack.append(b)
            if b == ")":
                if len(stack) > 0:
                    if stack[-1] != '(':
                        print("enter")
                        return False
                    else:
                        stack.pop()
                else: return False
            elif b == "]":
                if len(stack) > 0:
                    if stack[-1] != "[":
                        return False
                    else:
                        stack.pop()
                else: return False
            elif b == "}":
                if len(stack) > 0:
                    if stack[-1] != "{":
                        return False
                    else:
                        stack.pop()
                else: return False

        if len(stack) == 0:
            return True
        else:
            return False
