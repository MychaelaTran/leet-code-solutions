class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = - 1000000
        l = 0
        r =  k - 1
        if len(nums) == k: 
            total = sum(nums)
            return total/k

        temp = 0          
        while l <= len(nums) - k:
            if l == 0:
                for i in range(k): 
                    temp += nums[l+i]
            else: 
                temp -= nums[l-1]
                temp += nums[l+ k -1]
           
            temp = temp / k
            if temp > ans: 
                ans = temp
            temp = temp * k
            l += 1
        
        return ans
        