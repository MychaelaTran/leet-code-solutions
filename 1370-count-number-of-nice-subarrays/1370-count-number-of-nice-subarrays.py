class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #3ptr sliding window 
        left = 0 
        mid = 0 
        ans = 0
        odd_cnt = 0

        for right in range(len(nums)):
            if nums[right] % 2: 
                odd_cnt += 1
            
            while odd_cnt > k: 
                if nums[left] % 2 == 1: 
                    odd_cnt -= 1
                left += 1
                mid = left 

            if odd_cnt == k:
                while nums[mid] % 2 != 1: 
                    mid += 1
                ans += (mid - left) + 1

        return ans

        # count = 0 
        # for start in range(len(nums)): 
        #     odd_count =  0
        #     for end in range(start,len(nums)): 
        #         if nums[end] % 2 == 1: 
        #             odd_count += 1
                
        #         if odd_count == k: 
        #             count += 1
                
        #         if odd_count > k: 
        #             break

        # return count
                

        