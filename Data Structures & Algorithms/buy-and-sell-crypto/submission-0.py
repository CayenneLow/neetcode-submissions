class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        i = 0
        while i < len(prices):
            j = i + 1
            while j < len(prices):
                profit = prices[j] - prices[i]
                highest = max(highest, profit)
                j += 1
            i += 1
        return highest