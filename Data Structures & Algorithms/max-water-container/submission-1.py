class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        int_maxAreaSoFar = float("-inf")
        while l < r:
            int_curWidth = r - l
            int_minHeight = min(heights[l], heights[r])
            int_maxAreaSoFar = max(int_maxAreaSoFar, int_minHeight*int_curWidth)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return int_maxAreaSoFar
