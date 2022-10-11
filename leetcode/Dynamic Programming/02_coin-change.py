# Dynamic Programming - coin-change - https://leetcode.com/problems/coin-change/submissions/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = 0
        dp = [amount+1 for i in range(amount+1)]
        dp[0] = 0
        
        for i in range(1, amount+1) :
            for j in range(len(coins)) :
                if i - coins[j] >= 0 :
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        
        if dp[amount] == amount + 1 :
            return -1
        else :
            return dp[amount]
