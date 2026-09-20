#copy-paste from ai...

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0

        for sell in prices:
            maxProfit = max(maxProfit, sell - buy)
            buy = min(buy, sell)

        return maxProfit
