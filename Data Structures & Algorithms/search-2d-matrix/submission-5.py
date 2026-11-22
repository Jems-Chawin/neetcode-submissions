class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        # binary searching rows
        while t <= b:
            m_h = (t + b) // 2
            mid_row = matrix[m_h]
            if mid_row[0] <= target <= mid_row[-1]:
                # binary searching cols
                while l <= r:
                    m = (l + r) // 2
                    mid_val = mid_row[m]
                    if target == mid_val:
                        return True
                    if target > mid_val:
                        l = m + 1
                    else:
                        r = m - 1
                return False
            if target < mid_row[0]:
                b = m_h - 1
            else:
                t = m_h + 1
        return False