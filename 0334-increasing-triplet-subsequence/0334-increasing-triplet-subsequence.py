class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: 
            return False
        small = 1000000000000
        mid = 1000000000000

        for num in nums:
            if num > mid: 
                return True
            if num <= small: 
                small = num
            else:  #if num > small and num <= mid  
                mid = num 
        
        return False
                    

    #.  20  1000  10  12  5  13
    #.  10  1000  5  12  20  13

            