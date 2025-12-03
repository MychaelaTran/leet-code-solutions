class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        
        # Pointer for the end of the merged array
        p = m + n - 1
        
        # While there are elements to be processed in nums2
        while p2 >= 0:
            # If nums1 still has elements and nums1's element is larger
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Otherwise, take from nums2
                nums1[p] = nums2[p2]
                p2 -= 1
            # Move the write pointer backwards
            
            p -= 1

        return nums1