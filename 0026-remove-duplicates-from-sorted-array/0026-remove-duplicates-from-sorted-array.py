class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        duplicates = set()
        for i in range(1,len(nums)): 
            if nums[i] != nums[count -1]:
                count += 1
                nums[count-1] = nums[i]
                
          

            
   
        print(nums)
        return count
        