class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #are we extending sub arry or start over
        #start over when we add num and that num is > than curr sum 
        curr_sum = 0
        largest = nums[0]

        for num in nums: 
            curr_sum = max(curr_sum + num, num)
            largest = max(curr_sum, largest)
  
        return largest

        