class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ans = 0 
        if k == 0: 
            for key, value in count.items(): 
                if value > 1: 
                    ans += 1
        else: 
            for key,value in count.items():
                if key + k in count: 
                    ans += 1 #only one for unique 
        
        return ans
       
       
       
       
        # #brute force
        # pairs = [] 
        # ans = 0
        # for fst in range(len(nums)): 
        #     for snd in range(fst + 1, len(nums)): 
        #         differnce = nums[fst] - nums[snd]
        #         if abs(differnce) == k: 
        #             if [nums[fst], nums[snd]] not in pairs and [nums[snd], nums[fst]] not in pairs: 
        #                 print("pair added ", [nums[fst], nums[snd]])
        #                 pairs.append([nums[fst], nums[snd]])
        #                 ans += 1

        # return ans