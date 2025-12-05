class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #ptrs for nums1 and nums2
        p1 = m - 1
        p2 = n -1
        total = len(nums1) -1

        while total >= 0 and p1 >= 0 and p2 >= 0: 
            if nums1[p1] > nums2[p2]: 
                nums1[total] = nums1[p1]
                p1 -= 1
                total -=1
                
            else: 
                 nums1[total] = nums2[p2]
                 p2 -= 1 
                 total -= 1
        
        while p1 >= 0: 
            nums1[total] = nums1[p1]
            total -= 1
            p1 -= 1

        while p2 >= 0: 
            nums1[total] = nums2[p2]
            total -= 1
            p2 -= 1

       
