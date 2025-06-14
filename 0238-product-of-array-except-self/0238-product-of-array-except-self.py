class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        zero_count = 0
        ans = [0 for _ in range(len(nums))]
        for num in nums: 
            if num == 0: 
                zero_count += 1
                continue
            product_all *= num
        
        if zero_count > 1: 
            return ans
        
        print(product_all)
        
        for i in range(len(nums)):
            if zero_count == 1: 
                if nums[i] != 0: 
                    continue
                else: 
                    ans[i] = product_all
            else: 
                num_add = product_all//nums[i]
                ans[i] = num_add
            
        return ans
        