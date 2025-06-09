class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ans = [-1 for _ in range(len(queries))]
        my_hash = {}
        count = 0
        for i in range(len(nums)): 
            if nums[i] == x: 
                count += 1
                my_hash[count] = i # {occurence of x : index in i }
        
        for i in range(len(queries)): 
            if queries[i] in my_hash:
                ans[i] = my_hash[queries[i]] 

        return ans