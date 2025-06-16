class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #only delete one elment 
        #sliding window
        left = 0
        ans = 0
        temp = 0
        used = False
        for right in range(len(nums)): 
            if nums[right] == 1: 
                temp += 1 #add to count when see 1
                continue
            else:
                if not used: #if havent deleted one, can delete and continue
                    used = True
                    continue
                else:  #alr deleted a 0
                    if temp > ans: 
                        ans = temp #update ans
                    while nums[left] != 0:  #move windown until we hit a zero to be able to delete a 0 again
                        left += 1
                        temp -= 1 #minus 1 each time bc this is moving pass 1's
                    left += 1 #move the left up not because done dealing wioth current 0
                    used = True #and have used our flip 

        if temp > ans and used: 
            return temp
        
        if not used:  #if never flipped still need to delet eone
            return temp -1
        
        return ans
                

        