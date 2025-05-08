class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1)
        print(nums2)
        i = 0
        j = 0    
        total = 0
        answer = [0] * (m + n)
        while i < m and j < n:
            #merge
            if nums1[i] <= nums2[j]:
                print("num1 is smaller")
                answer[total] = nums1[i]
                total += 1
                i += 1
                print("this is i", i)
                print("this si answer", nums1)
            else: 
                print("num2 is smaller")
                answer[total] = nums2[j]
                total += 1
                j += 1
                print("this is j", j)
                print("this si answer", nums1)
        
        while (i < m):
            answer[total] = nums1[i]
            i += 1
            total += 1
        

        while j < n:
            answer[total] = nums2[j]
            j += 1
            total += 1

        for i in range(m + n):
            nums1[i] = answer[i]


        return nums1