class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        int_leftMAXsofar, int_rightMAXsofar = height[l], height[r]
        int_return = 0

        while l < r:
            if int_leftMAXsofar < int_rightMAXsofar:
                l += 1
                int_leftMAXsofar = max(int_leftMAXsofar, height[l])
                int_return += int_leftMAXsofar - height[l]
            else:
                r -= 1
                int_rightMAXsofar = max(int_rightMAXsofar, height[r])
                int_return += int_rightMAXsofar - height[r]
        
        return int_return
            