class Solution:
    def climbStairs(self, n: int) -> int:
        #creating our memo
        memo = [-1] * (n+1)  

        return self.helper(n, memo)
        

    def helper(self, n, memo):
        if n <= 2: 
            return n
        if memo[n] != -1: 
            return memo[n]

        
        memo[n] = self.helper(n -1, memo) + self.helper(n-2, memo)
           
    
        return memo[n]     