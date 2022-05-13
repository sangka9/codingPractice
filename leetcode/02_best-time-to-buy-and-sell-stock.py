# Array - best-time-to-buy-and-sell-stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        
        if len(prices) > 1 :
            while right < len(prices) :
                if prices[right] > prices[left] :
                    if prices[right] - prices[left] > profit :
                        profit = prices[right] - prices[left]
                else :
                    left = right
                right += 1
        
        return profit
