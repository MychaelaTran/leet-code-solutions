class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        } 
        prev = 0
        for char in reversed(s): #loop backward to see subtraction 
            num = roman[char]
            if num < prev: 
                total -= num
            else: 
                total += num
                prev = num


        return total 

        