# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        for index in range(1, len(prices)):
            if(prices[index] > buy):
                if profit < (prices[index] - buy):
                    profit = prices[index] - buy
            else:
                buy = prices[index]
                
        return profit
    
# Time complexity: O(n)
# Space complexity: O(1)