class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low = 1
        high = x // 2

        while low <= high:
            mid = (low + high) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1

        return high

        #26
        #mid : 13
        # lo =0 high = 12, mid = 6
        #6x6=36, high = 5, lo = 0
        #mid = 2, lo = 3, hi = 5
        #lo = 4, high = 5
        #lo = 5, high = 5
        #lo = 6, high = 5
