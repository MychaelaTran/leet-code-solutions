class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #only delete one elment 
        left = 0
        ans = 0
        temp = 0
        used = False
        for right in range(len(nums)): 
            if nums[right] == 1: 
                temp += 1
                continue
            else:
                if not used: 
                    used = True
                    continue
                else: 
                    if temp > ans: 
                        ans = temp
                    while nums[left] != 0: 
                        left += 1
                        temp -= 1
                    left += 1
                    used = True

        if temp > ans and used: 
            return temp
        
        if not used: 
            return temp -1
        
        return ans
                
                
        

        return ans

        