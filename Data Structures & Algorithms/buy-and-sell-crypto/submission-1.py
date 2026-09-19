class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        int_MAXprofit = 0
        int_MINsofar = float("inf")
        for i in prices:
            int_MINsofar = min(int_MINsofar, i)
            int_profit = i - int_MINsofar
            int_MAXprofit = max(int_MAXprofit, int_profit)
        return int_MAXprofit
