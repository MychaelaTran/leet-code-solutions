class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}
        for i, num in enumerate(nums):  #makes (index, value) pairs
            toFind = target - num
            if toFind in numMap: 
                return [numMap[toFind], i]
            numMap[num] = i
        return []