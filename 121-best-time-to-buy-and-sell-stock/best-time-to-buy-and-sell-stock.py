class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # Left  for buy
        r = 1 # Right for sell
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP , profit)
            else:
                l = r
            r += 1

        return maxP