class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # stores the last index of each character
        max_len = 0
        start = 0  # left bound of sliding window

        for end in range(len(s)):
            ch = s[end]

            if ch in char_index and char_index[ch] >= start:
                # move start to right of last occurrence of ch
                start = char_index[ch] + 1

            char_index[ch] = end
            max_len = max(max_len, end - start + 1)

        return max_len
