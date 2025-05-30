class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #booyer moore  voting algorithm 
        count = 0 
        temp = -1 
        
        #try to find the majority element 
        for i in range(len(nums)):
            if count == 0:
                temp = nums[i]
                count = 1
            else:
                if nums[i] == temp:
                    count +=1
                else: 
                    count -= 1

        return temp        