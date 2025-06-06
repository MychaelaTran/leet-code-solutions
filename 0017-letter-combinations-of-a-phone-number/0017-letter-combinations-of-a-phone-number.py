from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #if empty, returtn nothing 
        if not digits:
            return []

        #hashing 
        hash_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        ans = []

        def backtrack(index: int, curr_combo: str):
            #add once at final figit 
            if index == len(digits):
                ans.append(curr_combo)
                return

            #get digits and alll its letters
            curr_digit = digits[index]
            letters = hash_map[curr_digit]

            #do each letter and then next digit 
            for letter in letters:
                backtrack(index + 1, curr_combo + letter)

        #start backtacking 
        backtrack(0, "")
        return ans 
