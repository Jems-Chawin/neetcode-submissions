class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            h_l, h_r = heights[l], heights[r]
            w = r - l
            h = min(h_l, h_r)
            area = w * h
            max_area = max(max_area, area)
            if h_l < h_r:
                l += 1
            else:
                r -= 1
        return max_area