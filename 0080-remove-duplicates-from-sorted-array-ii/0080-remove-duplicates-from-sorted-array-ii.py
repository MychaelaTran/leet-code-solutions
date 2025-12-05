class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n
        #sliding window
        
        #first index always valid 
        write_index = 1 
        count = 1 

        for i in range(1, n):            
            #update count 
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1  #find a new number, reset count (non-decr order)
            
            #havent seen number more than twice, then we can wriote it 
            if count <= 2:
                nums[write_index] = nums[i]
                write_index += 1
            #if we have seen it more than twice, don't uipdate write index, 
            #write the next valid num there 
                
        return write_index