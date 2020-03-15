# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices)>1:
            minPrice = prices[0]
            for i in range(1,len(prices)):
                if minPrice<=prices[i]:
                    minPrice = prices[i]
                else:
                    maxProfit=max(maxProfit,prices[i]-minPrice)
        return maxProfit