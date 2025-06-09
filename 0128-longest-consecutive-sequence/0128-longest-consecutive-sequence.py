class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) #removes dplicates
        longest = 0

        for num in num_set:
            #get a new start to check from
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
