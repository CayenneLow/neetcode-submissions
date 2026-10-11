class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currMin = prices[0]
        for p in prices:
            maxProfit = max(maxProfit, p - currMin)
            currMin = min(currMin, p)
        return maxProfit