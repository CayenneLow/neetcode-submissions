class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #minL = [0, 10, 1, 1, 1, 1]
        #maxR = [7,  7, 7, 7, 1, 0]
        #
        #minL = [0, 1, 1, 1, 1, 1,]
        minL = [0] * len(prices)
        maxR = [0] * len(prices)

        min_so_far = 200
        i = 0
        while i < len(prices):
            min_so_far = min(prices[i], min_so_far)
            minL[i] = (min_so_far)
            i += 1

        max_so_far = 0
        i = len(prices) - 1
        while i >= 0:
            max_so_far = max(prices[i], max_so_far)
            maxR[i] = (max_so_far)
            i -= 1
        
        max_profit = 0
        i = 0
        while i < len(prices):
            max_profit = max(max_profit, maxR[i] - minL[i])
            i += 1
        print(minL)
        print(maxR)

        return max_profit