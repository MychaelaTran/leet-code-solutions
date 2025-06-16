class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = 0
        ans = -100000
        for i in range(len(gain)): 
            temp = temp + gain[i]
            if temp > ans: 
                ans = temp

        return max(ans,0)