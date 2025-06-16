class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first = []
        second = []
        ans = []
        set_1 = set(nums1)
        set_2 = set(nums2)
        
        for i in range(len(nums1)): 
            if nums1[i] in set_2: 
                continue
            else: 
                if nums1[i] in first: 
                    continue
                else: 
                    first.append(nums1[i])

        for i in range(len(nums2)): 
            if nums2[i] in set_1: 
                continue
            else: 
                if nums2[i] in second: 
                    continue
                else: 
                    second.append(nums2[i])
        
        ans.append(first)
        ans.append(second)
        return ans
