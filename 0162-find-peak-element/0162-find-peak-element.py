class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #modified BS where cut array in half by going in direction of GREATER side bc that side
        #is guranteed to have a peak element 
        low, high = 0, len(nums) -1

        while low <= high:
            mid = (low + high)//2

            #if left neighbour greater
            if mid > 0 and nums[mid-1] > nums[mid]:
                high = mid - 1
            #right neighbour greater 
            elif mid < len(nums) - 1 and nums[mid +1] > nums[mid]:
                low = mid + 1
            else:
                return mid