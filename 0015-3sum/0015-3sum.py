class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort to use two poitner 
        n = len(nums) -1 
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  #dont couhtn duplicate again 

            left = i + 1
            right = n

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    #skip diplicates 
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1 #go next uuniqye number 
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
