class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        count = 0 
        l = 0
        r = len(nums) -1
        
        while l < r: 
            total = nums[l] + nums[r]
            if total == k:
                count += 1
                l += 1
                r -= 1
            elif total < k:
                l += 1
            else:  # total > k
                r -= 1
        return count
        