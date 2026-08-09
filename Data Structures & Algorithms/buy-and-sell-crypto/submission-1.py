class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2: return 0
        l, r = 0,1
        maxProfit = 0
        for l in range(len(prices)):
            r = l + 1
            while r < len(prices):
                if prices[r] > prices[l]:
                    profit = prices[r] - prices[l]
                    maxProfit = max(profit,maxProfit)
                r += 1
        return maxProfit



