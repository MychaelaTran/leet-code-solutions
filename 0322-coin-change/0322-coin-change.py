class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #DP 
        #greedy fails, need DP to explore all possibilities efficently 
        max_val = amount + 1
        list_size = amount + 1
        dp = [max_val] * list_size
        dp[0] = 0

        #look at every amount from 1 up to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    #look in memo array
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        #if dp[amount] is still the init value then means we found no combo
        return dp[amount] if dp[amount] != amount + 1 else -1
         




'''
dp[i] = min(dp[i], 1 + dp[i- coin])
'''


        