class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        set_1 = set(nums1)
        set_2 = set(nums2)
        first = list(set_1 - set_2)
        second = list(set_2 - set_1)
        
        
        
        ans.append(first)
        ans.append(second)
        return ans
