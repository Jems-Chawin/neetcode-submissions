class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0

        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        rain = 0

        while l < r:
            if max_l <= max_r:
                l += 1
                cur_l = height[l]
                max_l = max(max_l, cur_l)
                rain += max_l - cur_l
            else:
                r -= 1
                cur_r = height[r]
                max_r = max(max_r, cur_r)
                rain += max_r - cur_r

        return rain