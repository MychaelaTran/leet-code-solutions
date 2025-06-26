class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
            
        if n == 0: 
            return nums1

        one = m - 1
        two = n - 1
        total = m + n - 1
        while one >= 0 and two >= 0: 
            if nums2[two] > nums1[one]: 
                nums1[total] = nums2[two]
                two -= 1
                total -= 1
            else: 
                nums1[total] = nums1[one]
                one -= 1
                total -= 1
        if one >= 0: 
            while one >= 0: 
                nums1[total] = nums1[one]
                one -=1 
                total -=1
        
        if two >= 0: 
            while two >= 0: 
                nums1[total] = nums2[two]
                two -=1 
                total -=1
                

        return nums1