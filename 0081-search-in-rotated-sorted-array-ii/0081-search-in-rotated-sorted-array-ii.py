class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        high = len(nums) -1
        low = 0

        while low <= high: 
            mid = (low + high) //2
            if nums[mid] == target: 
                return True

            #igf cant decide which half is sorted due to duplicates, shrink both sides (edge case [1,0,1,1,1])
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1

            #left subarray sorted:
            elif nums[low] <= nums[mid]:  
                if nums[low] <= target <= nums[mid]: 
                    high = mid - 1
                else: 
                    low = mid + 1
            
            #right array sorted (since left isnt) 
            else: 
                if nums[mid] <= target <= nums[high]: 
                    low = mid + 1
                else: 
                    high = mid - 1
            
        
        return False

        