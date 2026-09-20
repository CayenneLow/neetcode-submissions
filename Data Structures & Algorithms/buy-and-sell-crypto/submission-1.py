class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        l = 0
        r = 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            highest = max(highest, profit)
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r += 1
        return highest