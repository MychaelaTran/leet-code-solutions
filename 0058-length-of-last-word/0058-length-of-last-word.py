class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reverse = s[::-1]
        print(reverse)
        length = 0
        for char in reverse: 
            if char == " " and length != 0: 
                return length
            else: 
                if char != " ": 
                    length += 1
        return length
        