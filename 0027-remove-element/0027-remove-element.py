class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums) 
        
        while i < n:
            if nums[i] == val:
                #overwrite the bad elemmetn with last element 
                nums[i] = nums[n - 1]
                #"delete" the invalid spot
                n -= 1
                #dont increment i because we need to checkl if the number we just swapped with is valid 
            else:
                #if not val then can move to next element 
                i += 1
                
        return n