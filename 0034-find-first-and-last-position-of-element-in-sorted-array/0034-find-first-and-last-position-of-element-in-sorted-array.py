class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #binary search 
        #1st find elemetn with bin serarch
        #2nd do bin search on each half array until lowest and highest found 
        if len(nums) == 1 and target == nums[0]: 
            return [0,0]

        low = 0
        high = len(nums) - 1
        split = -1

        #finding elemet first 
        while low <= high: 
            mid = (high + low)//2
            if nums[mid] == target: 
                split = mid
                break
            elif nums[mid] > target: 
                high = mid - 1
            else: 
                low  = mid + 1
        
        if split == -1: 
            return [-1, -1]
        print(split)

        #now we have the first occurence of target
        #do binary serach in left and right halves

        #left half to find lowest index 
        left_low = 0
        left_high = split
        ans_low = split
        while left_low <= left_high: 
            mid = (left_low + left_high) //2
            if nums[mid] == target: 
                ans_low = mid
                left_high = mid -1
            elif nums[mid] < target: 
                left_low = mid + 1
            else: 
                left_high =  mid - 1
        
        print(ans_low)

        #right half to find lowest index 
        right_low = split
        right_high = len(nums) -1 
        ans_high = split
        while right_low <= right_high: 
            mid = (right_low + right_high) //2
            if nums[mid] == target: 
                ans_high = mid
                right_low = mid + 1
            elif nums[mid] < target: 
                right_low = mid + 1
            else: 
                right_high =  mid - 1
        
        print(ans_high)

        return [ans_low, ans_high]

