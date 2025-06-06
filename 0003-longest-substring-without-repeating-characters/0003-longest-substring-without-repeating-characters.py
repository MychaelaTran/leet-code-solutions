class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # Optimal Hashing + Sliding Window Solution
        char_index = {} #stores letter:index
        window_start = 0
        ans = 0

        for i in range(len(s)):
            letter = s[i]
            if letter in char_index and char_index[letter] >= window_start: 
                window_start = char_index[letter] + 1
            
            char_index[letter] = i
            ans = max(ans, i-window_start + 1)


        return ans

'''
abcab

i = 0 | {a: 0} | max = 1 | window a
i = 1 | {a:0, b:1} max = 2  | window ab
i = 3 | {a:0. b:1, c:2} | max = 3  | window abc
i = 4 ~ a is in hash , move window up from left to get rid of duplicate | window bca | {a: 3, b:1. c: 3} | max = 3
'''