class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = float("inf")
        for p in prices:
            # หา min แล้วก็เก็บ profit ไล่ไปจนกว่าจะมี min ที่น้อยกว่า หรือ profit มากกว่า
            min_so_far = min(min_so_far, p)
            cur_profit = p - min_so_far
            # แต่ max profit ต้องดูว่า max กว่าตัวเดิมไหม
            max_profit = max(max_profit, cur_profit)
        return max_profit