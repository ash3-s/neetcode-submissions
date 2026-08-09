class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices)):
            maxP = 0
            if i > 0 and prices[i] - prices[i - 1] > 0:
                profit = prices[i] - prices[i - 1]
                res += profit
        return res
