class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 2.5: 
            division = n/2
            if division - 0.5 == floor(n/2): #means has .5 at end
                ans += 1
            n = floor(n/2)
        
        ans += 1
        
        return ans
        
        