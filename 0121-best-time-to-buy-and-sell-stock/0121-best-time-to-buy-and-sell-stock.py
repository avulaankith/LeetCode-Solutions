class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 11111111111
        profit = 0
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            else:
                profit = max(profit, prices[i]-mini)
        return profit