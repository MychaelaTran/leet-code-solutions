class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        temp = 0
        left = 0
        counter = k 
        temp = 0

        for right in range(len(nums)): 
            if nums[right] == 1: 
                temp += 1
                continue
            
            if counter > 0: 
                temp += 1
                counter -= 1
            else: 
                if temp > ans: 
                    ans = temp
                while counter == 0:
                    if nums[left] == 0:
                        counter += 1
                    temp -= 1
                    left += 1
                temp += 1
                counter -= 1

                
                    

        if temp > ans: 
            ans = temp
        return ans
