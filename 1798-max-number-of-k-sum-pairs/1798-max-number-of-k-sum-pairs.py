class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        count = 0 
        l = 0
        r = len(nums) -1
        
        while l < r: 
            to_find = k - nums[l]
            if nums[r] == to_find: 
                count += 1
                l += 1
                r -= 1
            elif nums[r] > to_find: 
                r -=1
            else: 
                l += 1
                to_find = k - nums[l]
        return count
        