class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float("inf")
        max_profit = 0
        for i in prices:
            min_so_far = min(i, min_so_far)
            profit = i - min_so_far
            max_profit = max(profit, max_profit)
        return max_profit