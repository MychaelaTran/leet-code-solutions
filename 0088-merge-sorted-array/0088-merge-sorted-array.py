class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #need to merge from the back, to modify nums1 in place
        i = m -1
        j = n - 1
        total = m + n - 1

        while i >= 0  and j >=0: 
            if nums1[i] >= nums2[j]:
                nums1[total] = nums1[i]
                total -= 1
                i -= 1
            else: 
                nums1[total] = nums2[j]
                total -= 1
                j -= 1
        
        while i >=0: 
            nums1[total] = nums1[i]
            total -= 1
            i -= 1
        
        while j >= 0: 
            nums1[total] = nums2[j]
            total -= 1
            j -= 1



        return nums1