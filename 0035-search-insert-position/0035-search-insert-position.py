class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        if target < nums[0]:
            return 0


        while low <= high:
            mid = (high + low)//2
            if nums[mid] > target:
                high = mid -1
            elif nums[mid] < target: 
                low = mid + 1
            else: 
                return mid 
        
        if target > low:
            return low
        else: 
            return high + 1
            