class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = float("-inf")
        while l < r:
            cur_width = r - l
            min_h = min(heights[l], heights[r])
            # max area จะขึ้นกับ min heights และความกว้าง ณ ตอนนั้น
            max_area = max(max_area, cur_width * min_h)
            # จะเอาที่เป็นไปได้ว่าจะ max area ที่สุด ก็ต้อง heights สูงขึ้นเรื่อยๆ
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
