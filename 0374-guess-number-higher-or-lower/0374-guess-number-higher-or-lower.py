# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            mid = (high + low)//2
            hint = guess(mid)
            
            if hint == -1: 
                high = mid -1
            elif hint == 1: 
                low = mid + 1
            else: 
                return mid
        
        return low
            
        