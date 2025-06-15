class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #starting usm 
        temp = sum(nums[:k])
        ans = temp

        #sliding window part 
        for l in range(1, len(nums) - k + 1):
            temp = temp - nums[l-1] + nums[l+k-1]
            ans = max(ans, temp)

        return ans / k
